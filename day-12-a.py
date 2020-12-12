import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
facing = 0
facing_dirs = {0:'E',90:'N',180:'W',270:'S'}
posn = [0,0] # east, north (neg numbers = west, south)

for line in data:
  command = line[0]
  amount = int(line[1:])
  if command == 'F':
    command = facing_dirs[facing]
  if command == 'N':
    posn[1] += amount
  if command == 'S':
    posn[1] -= amount
  if command == 'E':
    posn[0] += amount
  if command == 'W':
    posn[0] -= amount
  if command == 'L':
    facing += amount
    facing = facing % 360
  if command == 'R':
    facing -= amount
    facing = facing % 360

print(abs(posn[0]) + abs(posn[1]))
