import sys

data = [line.rstrip().split() for line in sys.stdin.readlines()]
#data = ['1-3 a: abcde'.split(),'1-3 b: cdefg'.split(),'2-9 c: ccccccccc'.split()]

num_valid = 0
for line in data:
    range = [int(n) for n in line[0].split('-')]
    letter = line[1][0]
    pw = line[2]
    num_found = len([ch for ch in pw if ch==letter])
    if num_found >= range[0] and num_found <= range[1]:
        num_valid += 1
    print (range, letter, pw, num_found)

print (num_valid)
