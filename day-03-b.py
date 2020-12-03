import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
height = len(data)
width = len(data[0])

answer = 1
for choice in [ (1,1),(3,1),(5,1),(7,1),(1,2) ]:
    num_trees = 0
    x = 0
    y = 0
    x_incr = choice[0]
    y_incr = choice[1]
    while y < height-y_incr:
        y += y_incr
        x += x_incr
        if x > width - 1:
            x = x % width
        if data[y][x] == '#':
            num_trees += 1
    answer = answer * num_trees
print (answer)
