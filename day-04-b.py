import sys
import re

data = [line.rstrip() for line in sys.stdin.readlines()]
passports = []
current_passport = {}
for line in data:
  if len(line) == 0:
    passports.append(current_passport)
    current_passport = {}
    continue
  for item in line.split():
    [k,v] = item.split(':')
    current_passport[k] = v
passports.append(current_passport)

def test_byr(byr):
  return re.match('^\d{4}$', byr) and int(byr) >= 1920 and int(byr) <= 2002

def test_iyr(iyr):
  return re.match('^\d{4}$', iyr) and int(iyr) >= 2010 and int(iyr) <= 2020

def test_eyr(eyr):
  return re.match('^\d{4}$', eyr) and int(eyr) >= 2020 and int(eyr) <= 2030

def test_hgt(hgt):
  if re.match('^\d{3}cm$', hgt):
    n = int(hgt[:3])
    return n >= 150 and n <= 193
  if re.match('^\d{2}in$', hgt):
    n = int(hgt[:2])
    return n >= 59 and n <= 76
  return False

def test_hcl(hcl):
  return re.match('^\#[0-9a-f]{6}$', hcl)

def test_ecl(ecl):
  return ecl in 'amb blu brn gry grn hzl oth'.split()

def test_pid(pid):
  return re.match('^\d{9}$', pid)

num_valid_passports = 0
for passport in passports:
  is_present = True
  for req_key in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
    if not req_key in passport.keys():
      is_present = False
      break
  if not is_present:
    continue
  is_valid = test_byr(passport['byr']) and \
             test_iyr(passport['iyr']) and \
             test_eyr(passport['eyr']) and \
             test_hgt(passport['hgt']) and \
             test_hcl(passport['hcl']) and \
             test_ecl(passport['ecl']) and \
             test_pid(passport['pid'])
  if is_valid:
    num_valid_passports += 1

print(num_valid_passports)

