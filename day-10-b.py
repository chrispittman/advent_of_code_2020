import sys

data = [int(line.rstrip()) for line in sys.stdin.readlines()]
data.sort()
data = [0] + data + [data[-1] + 3]
adapter_path_counts = { d:0 for d in data }
adapter_path_counts[data[-1]] = 1

for d in data[::-1]:
  for dist in [1,2,3]:
    if d+dist in adapter_path_counts:
      adapter_path_counts[d] += adapter_path_counts[d+dist]

print (adapter_path_counts[0])
