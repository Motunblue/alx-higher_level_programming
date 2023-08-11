#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

length = len(argv) - 1
if (length > 1):
    print("{} arguments:".format(length))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
elif (length == 1):
    print("1 argument:")
    print("{}: {}".format(length, argv[length]))
else:
    print("0 arguments.")
