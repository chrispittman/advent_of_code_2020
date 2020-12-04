import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
passports = []
current_passport = {}
for line in data:
  if len(line) == 0:
    passports.append(current_passport)
    current_passport = {}
    continue
  items = line.split()
  for item in items:
    [k,v] = item.split(':')
    current_passport[k] = v
passports.append(current_passport)

num_valid_passports = 0
for passport in passports:
  is_valid = True
  for req_key in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
    if not req_key in passport.keys():
      is_valid = False
  if is_valid:
    num_valid_passports += 1

print(num_valid_passports)
