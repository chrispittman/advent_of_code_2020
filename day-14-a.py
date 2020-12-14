import sys

data = [line.rstrip().split(' = ') for line in sys.stdin.readlines()]

mask = '0'
memory = {}
for (command,arg) in data:
  if command == 'mask':
    mask = arg
  else:
    binary = list(bin(int(arg))[2:].zfill(36))
    for i in range(len(mask)):
      if mask[i] != 'X':
        binary[i] = mask[i]
    binary = ''.join(binary)
    memory[command] = int(binary,2)
print(sum(memory.values()))
