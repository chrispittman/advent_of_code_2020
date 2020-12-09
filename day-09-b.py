import sys

data = [int(line.rstrip()) for line in sys.stdin.readlines()]
window_length = 25

invalid_number = None
for i in range(window_length, len(data)):
  prev_nums = data[i-window_length:i]
  found = False
  for j in range(len(prev_nums)):
    for k in range(j):
      if prev_nums[j] + prev_nums[k] == data[i]:
        found = True
  if not found:
    invalid_number = data[i]

for i in range(len(data)):
  for j in range(i-1):
    nums = data[j:i]
    if sum(nums) == invalid_number:
      print (max(nums)+min(nums))
