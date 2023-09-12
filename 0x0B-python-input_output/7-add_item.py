#!/usr/bin/python3
"""Add item Module"""
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

args = sys.argv[1:]

try:
    json_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    json_list = []

for a in args:
    json_list.append(a)

save_to_json_file(json_list, "add_item.json")
