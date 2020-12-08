import sys
import copy

orig_data = [line.rstrip().split() for line in sys.stdin.readlines()]
data = copy.deepcopy(orig_data)
acc = 0
posn = 0

def run_line():
  global posn, acc
  (inst, val) = data[posn]
  val = int(val)
  if inst == 'nop':
    posn += 1
  elif inst == 'acc':
    acc += val
    posn += 1
  elif inst == 'jmp':
    posn += val

for changed_line in range(len(data)):
  data = copy.deepcopy(orig_data)
  acc = 0
  posn = 0
  if data[changed_line][0] == 'acc':
    continue
  elif data[changed_line][0] == 'jmp':
    data[changed_line][0] = 'nop'
  elif data[changed_line][0] == 'nop':
    data[changed_line][0] = 'jmp'

  for num_ticks in range(10000):
    if posn < 0 or posn >= len(data):
      print('terminating, acc:', acc)
      break
    run_line()

