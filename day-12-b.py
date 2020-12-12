import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
waypoint = [10,1] # east, north
posn = [0,0] # east, north (neg numbers = west, south)

for line in data:
  command = line[0]
  amount = int(line[1:])
  if command == 'F':
    posn[0] += waypoint[0]*amount
    posn[1] += waypoint[1]*amount
  if command == 'N':
    waypoint[1] += amount
  if command == 'S':
    waypoint[1] -= amount
  if command == 'E':
    waypoint[0] += amount
  if command == 'W':
    waypoint[0] -= amount
  if command == 'L':
    command = 'R'
    amount = -amount
  if command == 'R':
    amount = amount % 360
    if amount==90:
      waypoint = [waypoint[1], -waypoint[0]]
    if amount==180:
      waypoint = [-waypoint[0], -waypoint[1]]
    if amount==270:
      waypoint = [-waypoint[1], waypoint[0]]

print(abs(posn[0]) + abs(posn[1]))
