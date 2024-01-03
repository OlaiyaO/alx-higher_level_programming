#!/usr/bin/python3

for i in range(ord('z'), ord('a') - 1, -1):
    diff = 0 if i % 2 == 0 else 32
    print('{}'.format(chr(i - diff)), end='')
