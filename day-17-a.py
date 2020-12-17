import sys

data = [line.rstrip() for line in sys.stdin.readlines()]

life = set()
for x in range(len(data)):
  for y in range(len(data)):
    if data[y][x] == '#':
      life.add((x,y,0))

neighbors = []
for i in [-1,0,1]:
  for j in [-1,0,1]:
    for k in [-1,0,1]:
      if i==j==k==0: continue
      neighbors.append( (i,j,k) )

def iterate(life):
  new_life = set()
  posns_to_check = set()
  for posn in life:
    for n in neighbors:
      posns_to_check.add( (posn[0]+n[0], posn[1]+n[1], posn[2]+n[2]) )

  for check_posn in posns_to_check:
    num_active_nearby = 0
    for n in neighbors:
      check_posn_neighbor = (check_posn[0]+n[0], check_posn[1]+n[1], check_posn[2]+n[2]) 
      if check_posn_neighbor in life:
        num_active_nearby += 1
    if check_posn in life:
      if num_active_nearby==2 or num_active_nearby==3:
        new_life.add(check_posn)
    else:
      if num_active_nearby==3:
        new_life.add(check_posn)
  return new_life

for i in range(6):
  life = iterate(life)

print(len(life))
