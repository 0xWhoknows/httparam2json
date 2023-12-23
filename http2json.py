import json
import argparse
from urllib.parse import parse_qs


def main() -> None:
    '''
    Process URL parameters and convert them to JSON format.

    Arguments:
        - -f, --input_file: Input file containing URL parameters.
        - -o, --output_file: Output file to save JSON data.
        - -jq, --json_query: JSON query string (e.g., '{"fname":"firstname","lname":"lastname"}').

    Usage examples:
        1. Process parameters from a file and print the JSON to the console:
           python3 httparam2json.py -f input.txt OR python3 httparam2json.py -jq '{"fname":"firstname","lname":"lastname"}'

        2. Process parameters from a JSON query and save the JSON to an output file:
           python3 httparam2json.py -jq '{"fname":"firstname","lname":"lastname"}' -o output.json

    '''
    parser = argparse.ArgumentParser(description="Process URL parameters.")
    parser.add_argument("-f", "--input_file", help="Input file containing URL parameters")
    parser.add_argument("-o", "--output_file", help="Output file to save JSON data")
    parser.add_argument("-jq", "--json_query", help="JSON query string (e.g., 'fname=firstname&lname=lastname')")

    args = parser.parse_args()

    if args.input_file:
        with open(args.input_file, 'r') as file:
            argument = file.read().strip()
    elif args.json_query:
        argument = args.json_query
    else:
        print("Usage: python httparam2json.py -jq 'fname=firstname&lname=lastname'")
        return


    parsed_url = parse_qs(argument)
    json_data = {key: values[0] for key, values in parsed_url.items() if values}
    json_str = json.dumps(json_data)

    if args.output_file:
        print(f"{json_str}")
        with open(args.output_file, 'w') as ww:
            ww.write(json_str)
    else:
        print(f"{json_str}")


if __name__ == "__main__":
    main()
