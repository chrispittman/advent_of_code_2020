import sys

data = [int(line.rstrip()) for line in sys.stdin.readlines()]
window_length = 25

for i in range(window_length, len(data)):
  prev_nums = data[i-window_length:i]
  found = False
  for j in range(len(prev_nums)):
    for k in range(j):
      if prev_nums[j] + prev_nums[k] == data[i]:
        found = True
  if not found:
    print (data[i])
