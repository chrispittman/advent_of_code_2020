import sys

data = [0,13,1,8,6,15]
#data = [2,1,3]

last_spoken = {}
for i in range(len(data)):
  last_spoken[data[i]] = (i,None)

num_turns = 30000000
for i in range(len(data),num_turns):
  n = data[-1]
  (last_posn, next_to_last_posn) = last_spoken[n]
  if next_to_last_posn is None:
    spoken = 0
  else:
    spoken = last_posn - next_to_last_posn
  data.append(spoken)
  last_spoken[spoken] = (i, last_spoken.get(spoken,(None,None))[0])
print(data[-1])
