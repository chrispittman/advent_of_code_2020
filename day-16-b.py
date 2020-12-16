import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
your_ticket_header = data.index('your ticket:')
nearby_ticket_header = data.index('nearby tickets:')
rule_lines = data[ 0 : your_ticket_header-1 ]
your_ticket_line = data[your_ticket_header+1]
nearby_ticket_lines = data[nearby_ticket_header+1:]

## Parse input
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
all_tickets = [your_ticket] + nearby_tickets

## For which rules is this a valid input?
def valid_choices(num, rules):
  choices = set()
  for key in rules.keys():
    if num in rules[key]:
      choices.add(key)
  return choices

## For all valid tickets, what are the valid options for each field?
field_options = [set(rules.keys()) for x in your_ticket]
for ticket in all_tickets:
  choices = [valid_choices(ticket[i],rules) for i in range(len(ticket))]
  if set() in choices:
    continue # ticket is invalid
  for i in range(len(ticket)):
    field_options[i] = field_options[i].intersection(choices[i])

## Resolve that matrix of options into a single option for each field
field_keys = [None for i in range(len(field_options))]
while None in field_keys:
  removed = None
  for i in range(len(field_options)):
    if len(field_options[i])==1:
      removed = list(field_options[i])[0]
      field_keys[i] = removed
      break
  for opt in field_options:
    if removed in opt:
      opt.remove(removed)

## Show which fields exist, and your ticket values for that field
for i in range(len(field_keys)):
  print(field_keys[i], ':', your_ticket[i])


