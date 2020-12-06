import sys
import itertools

data = sys.stdin.read().strip()
data = data.replace('\n\n','.').split('.')
num_people = [line.count('\n')+1 for line in data]
data = [line.replace('\n','') for line in data]

counts = []
for line in data:
  hist = {}
  for c in line:
    hist[c] = line.count(c)
  counts.append(hist)

result = 0
for c,req in list(zip(counts,num_people)):
  result += len([v for v in c.values() if v==req])
print (result)
