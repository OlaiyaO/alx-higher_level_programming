#!/usr/bin/python3
"""
Script to add arguments to a Python list and save them to a JSON file.
"""

import sys
import json
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if not path.exists(filename):
    with open(filename, 'w') as f:
        json.dump([], f)

my_list = load_from_json_file(filename)

for arg in sys.argv[1:]:
    my_list.append(arg)

save_to_json_file(my_list, filename)
