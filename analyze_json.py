import json

with open('demo3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

element_to_identifier = {}
identifier_to_elements = {}

for obj in data:
    eid = obj['element']['id']
    identifier = obj['identifier']
    element_to_identifier[eid] = identifier
    identifier_to_elements.setdefault(identifier, set()).add(eid)

# 检查一一对应
one_to_many = False
many_to_one = False
for identifier, eids in identifier_to_elements.items():
    if len(eids) > 1:
        print(f"identifier {identifier} maps to multiple element.ids: {eids}")
        one_to_many = True

identifier_count = {}
for eid, identifier in element_to_identifier.items():
    identifier_count.setdefault(identifier, 0)
    identifier_count[identifier] += 1

reverse_map = {}
for eid, identifier in element_to_identifier.items():
    reverse_map.setdefault(eid, set()).add(identifier)
for eid, ids in reverse_map.items():
    if len(ids) > 1:
        print(f"element.id {eid} maps to multiple identifiers: {ids}")
        many_to_one = True

if not one_to_many and not many_to_one and len(element_to_identifier) == len(identifier_to_elements):
    print("element.id and identifier are one-to-one corresponding.")
elif one_to_many and not many_to_one:
    print("identifier maps to multiple element.ids (one-to-many).")
elif many_to_one and not one_to_many:
    print("element.id maps to multiple identifiers (many-to-one).")
else:
    print("There are both one-to-many and many-to-one relationships.")