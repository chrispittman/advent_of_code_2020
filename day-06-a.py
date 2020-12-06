import sys
import itertools

data = sys.stdin.read()
data = data.replace('\n\n','.').replace('\n','').split('.')
data = [list(set(el)) for el in data]
data = list(itertools.chain(*data))
print (len(data))
