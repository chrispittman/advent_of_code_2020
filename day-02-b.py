import sys

data = [line.rstrip().split() for line in sys.stdin.readlines()]
#data = ['1-3 a: abcde'.split(),'1-3 b: cdefg'.split(),'2-9 c: ccccccccc'.split()]

num_valid = 0
for line in data:
    range = [int(n) for n in line[0].split('-')]
    letter = line[1][0]
    pw = line[2]
    # 'found in first posn' xor 'found in second position'
    found_first  = pw[range[0]-1] == letter
    found_second = pw[range[1]-1] == letter
    if found_first != found_second:
        num_valid += 1

print (num_valid)
