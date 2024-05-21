#!/usr/bin/python3
"""
Script to add command line arguments to a Python list,
save the list as a JSON representation in a file, and then load it back

Dependencies:
- load_from_json_file function from 6-load_from_json_file.py
- save_to_json_file function from 5-save_to_json_file.py
"""

if __name__ == "__main__":

    import sys
    load_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        my_list = load_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, "add_item.json")
