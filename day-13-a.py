import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
leave_time = int(data[0])
buses = [int(b) for b in data[1].split(',') if b != 'x']
buses.sort()

min_time_to_wait = 1000000
best_bus = 0
for bus in buses:
  (last_dep, time_ago) = divmod(leave_time, bus)
  time_to_wait = bus - time_ago
  if time_to_wait < min_time_to_wait:
    min_time_to_wait = time_to_wait
    best_bus = bus
print(min_time_to_wait * best_bus)
