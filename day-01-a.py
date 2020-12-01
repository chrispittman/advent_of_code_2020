import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(line) for line in data]

#data = [1721,979,366,299,675,1456]

for n in data:
    complement = 2020 - n
    if complement in data:
        print (n * complement)
        break
