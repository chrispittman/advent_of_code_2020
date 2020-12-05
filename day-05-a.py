import sys

data = [line.rstrip() for line in sys.stdin.readlines()]


result = 0
for bpass in data:
    fb = bpass[:7].replace('F','0').replace('B','1')
    row = int(fb,2)
    rl = bpass[-3:].replace('L','0').replace('R','1')
    seat = int(rl,2)
    id = row * 8 + seat
    result = max(result, id)
print (result)
