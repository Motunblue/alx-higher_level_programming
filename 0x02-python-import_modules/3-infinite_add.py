#!/usr//bin/python3
from sys import argv

sum = 0
length = len(argv) - 1
if length > 0:
    for i in range(1, length + 1):
        sum += int(argv[i])
print("{}".format(sum))
