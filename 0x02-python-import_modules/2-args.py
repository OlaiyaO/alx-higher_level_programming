#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

length = len(argv)
print("{} argument{}{}\n".format(length - 1,
                                 "s" if length != 2 else "",
                                 "." if length == 1 else ":"), end="")
if length > 1:
    for i in range(1, length):
        print("{}: {}".format(i, argv[i]))
else:
    pass
