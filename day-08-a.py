import sys

data = [line.rstrip().split() for line in sys.stdin.readlines()]

acc = 0
posn = 0
has_run = [0] * len(data)

def run_line():
  global posn, acc
  (inst, val) = data[posn]
  val = int(val)
  has_run[posn] = 1
  if inst == 'nop':
    posn += 1
  elif inst == 'acc':
    acc += val
    posn += 1
  elif inst == 'jmp':
    posn += val

for num_ticks in range(1000000):
  if has_run[posn]:
    print ('acc:', acc)
    break
  run_line()
