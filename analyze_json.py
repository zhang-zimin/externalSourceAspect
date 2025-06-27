import json

with open('demo.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

element_to_identifier = {}
identifier_to_element = {}
for obj in data:
    eid = obj['element']['id']
    identifier = obj['identifier']
    # 检查一一对应
    if eid in element_to_identifier and element_to_identifier[eid] != identifier:
        print(f"element.id {eid} maps to multiple identifiers: {element_to_identifier[eid]}, {identifier}")
    if identifier in identifier_to_element and identifier_to_element[identifier] != eid:
        print(f"identifier {identifier} maps to multiple element.ids: {identifier_to_element[identifier]}, {eid}")
    element_to_identifier[eid] = identifier
    identifier_to_element[identifier] = eid

if len(element_to_identifier) == len(identifier_to_element) == len(data):
    print("element.id and identifier are one-to-one corresponding.")
else:
    print("element.id and identifier are NOT one-to-one corresponding.")