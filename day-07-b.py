import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
data = [line.split(' bags contain ') for line in data]
rules = {}
for item in data:
  rules[item[0]] = item[1]

for bagtype in rules.keys():
  if rules[bagtype] == 'no other bags.':
    rules[bagtype] = None
  else:
    types = []
    for bag in rules[bagtype].split(', '):
      bag_parts = bag.split(' ')
      count = int(bag_parts[0])
      type = bag_parts[1] + ' ' + bag_parts[2]
      types.append((count,type))
    rules[bagtype] = types

def count_self_and_children(amt, type):
  if not rules[type]:
    return amt
  total = amt
  for rule in rules[type]:
    total += amt * count_self_and_children(rule[0], rule[1])
  return total

print(count_self_and_children(1,'shiny gold') - 1)

