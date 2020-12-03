import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
height = len(data)
width = len(data[0])

num_trees = 0
x = 0
y = 0
x_incr = 3
y_incr = 1
while y < height-y_incr:
   y += y_incr
   x += x_incr
   if x > width - 1:
       x = x % width
   if data[y][x] == '#':
       num_trees += 1
print (num_trees)
