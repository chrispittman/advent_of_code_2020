import sys
import copy

data = [[c for c in line.rstrip()] for line in sys.stdin.readlines()]
layout_height = len(data)
layout_width = len(data[0])
last_round = copy.deepcopy(data)

def get_thing_at_posn(layout, x, y):
  if x<0 or x>=layout_width or y<0 or y>=layout_height:
    return None
  return layout[y][x]

def get_adjacents(layout, x, y):
  bounds = [0, len(layout)]
  adj = [ [x-1,y-1], [x-1,y], [x-1,y+1], [x,y-1], [x,y+1], [x+1,y-1], [x+1,y], [x+1,y+1] ]
  result = ''
  for (adj_x,adj_y) in adj:
    neighbor = get_thing_at_posn(layout, adj_x, adj_y)
    if neighbor:
      result += neighbor
  return result

while True:
  this_round = copy.deepcopy(last_round)
  for y in range(layout_height):
    for x in range(layout_width):
      current_thing = get_thing_at_posn(last_round, x, y)
      neighbors = get_adjacents(last_round, x, y)
      if current_thing=='L' and neighbors.count('#')==0:
        this_round[y][x] = '#'
      elif current_thing=='#' and neighbors.count('#')>=4:
        this_round[y][x] = 'L'
#  for line in this_round:
#    print (''.join(line))
#  print('')
  if this_round == last_round:
    break
  last_round = this_round

print(sum([line.count('#') for line in this_round]))
