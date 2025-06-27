# Element JSON Analysis Project

This project provides scripts and tools to analyze the relationships between fields in a large JSON file (`demo.json`). Typical checks include verifying one-to-one correspondence between fields such as `id`, `element.id`, and `identifier`.

## Project Structure

- `demo.json` — The main JSON data file to be analyzed.
- `analyze_json.py` — Python script(s) for checking relationships between fields in the JSON file.

## Usage

1. Make sure you have Python 3 installed.
2. Place your `demo.json` file in the project directory.
3. Run the analysis script:
   ```sh
   python analyze_json.py
   ```
   The script will output whether the relationships (e.g., between `id` and `element.id`) are one-to-one and print any mismatches.

## Customization

- You can modify `analyze_json.py` to check other field relationships, such as between `element.id` and `identifier`.
- Adjust the script according to your JSON structure if your keys are different.

## Example Checks

- Are `id` and `element.id` one-to-one corresponding?
- Are `element.id` and `identifier` one-to-one corresponding?

## License

This project is for internal analysis and demonstration purposes.
