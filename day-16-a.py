import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
your_ticket_header = data.index('your ticket:')
nearby_ticket_header = data.index('nearby tickets:')
rule_lines = data[ 0 : your_ticket_header-1 ]
your_ticket_line = data[your_ticket_header+1]
nearby_ticket_lines = data[nearby_ticket_header+1:]

rules = {}
for rule in rule_lines:
  (key,desc) = rule.split(': ')
  rules[key] = []
  desc_parts = desc.split(' or ')
  for part in desc_parts:
    (lower,upper) = [int(x) for x in part.split('-')]
    for num in range(lower,upper+1):
      rules[key].append(num)
your_ticket = [int(x) for x in your_ticket_line.split(',')]
nearby_tickets = [[int(x) for x in line.split(',')] for line in nearby_ticket_lines]

error_rate = 0
for ticket in nearby_tickets:
  for value in ticket:
    valid = False
    for rule in rules.values():
      if value in rule:
        valid = True
    if not valid:
      error_rate += value
print(error_rate)
