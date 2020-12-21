import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
allergens = [line.split('(contains ')[1][:-1].split(', ') for line in data]
foods = [line.split(' (')[0].split() for line in data]

all_allergens = set()
for a in allergens:
  all_allergens = all_allergens.union(set(a))

all_ingredients = set()
for food in foods:
  all_ingredients = all_ingredients.union(set(food))

canon_ingreds = {}

for a in all_allergens:
  allergen_ingredients = all_ingredients.copy()
  for i in range(len(foods)):
    food = foods[i]
    allergen = allergens[i]
    if a in allergen:
      allergen_ingredients = allergen_ingredients.intersection(set(food))
  canon_ingreds[a] = allergen_ingredients

while True:
  single_choices = set()
  for i in canon_ingreds.values():
    if len(i) == 1:
      single_choices.add(list(i)[0])
  for k in canon_ingreds.keys():
    if len(canon_ingreds[k])>1:
      canon_ingreds[k] = canon_ingreds[k].difference(single_choices)
  is_done = True
  for i in canon_ingreds.values():
    if len(i) > 1:
      is_done = False
  if is_done:
    break

for k in canon_ingreds.keys():
  canon_ingreds[k] = list(canon_ingreds[k])[0]

sorted_keys = list(canon_ingreds.keys())
sorted_keys.sort()
answer = [canon_ingreds[k] for k in sorted_keys]

print(','.join(answer))
