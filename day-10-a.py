import sys

data = [int(line.rstrip()) for line in sys.stdin.readlines()]
data.sort()
data = [0] + data + [data[-1] + 3]

diffs = [None, 0, 0, 0]
for i in range(1,len(data)):
  diff = data[i] - data[i-1]
  diffs[diff] += 1
print(diffs[1] * diffs[3])
