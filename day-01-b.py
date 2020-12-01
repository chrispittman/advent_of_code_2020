import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [int(line) for line in data]

#data = [1721,979,366,299,675,1456]

for n1 in data:
    for n2 in data:
        for n3 in data:
            if n1+n2+n3 == 2020:
                print (n1 * n2 * n3)
                sys.exit(0)
