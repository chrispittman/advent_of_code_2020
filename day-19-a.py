import sys
import itertools
import re

data = [line.rstrip() for line in sys.stdin.readlines()]
[raw_rules,messages] = \
  [list(y) for x,y in itertools.groupby(data, lambda z:z=='') if not x]

rules = {}
for rule in raw_rules:
  [key,value] = rule.split(': ')
  rules[key] = value

def convert_to_regex(rule):
  spec = rules[rule]
  if spec[0] == '\"':
    return spec[1]
  result = '('
  for part in spec.split(' '):
    if part == '|':
      result += part
    else:
      result += convert_to_regex(part)
  result += ')'
  return result

regex = convert_to_regex('0')
matches = [m for m in messages if re.fullmatch(regex,m)]
print ( len(matches) )
