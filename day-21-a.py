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

safe_ingredients = all_ingredients.copy()
for a in all_allergens:
  allergen_ingredients = all_ingredients.copy()
  for i in range(len(foods)):
    food = foods[i]
    allergen = allergens[i]
    if a in allergen:
      allergen_ingredients = allergen_ingredients.intersection(set(food))
  safe_ingredients = safe_ingredients.difference(allergen_ingredients)

total_count = 0
for ingred in safe_ingredients:
  for food in foods:
    total_count += food.count(ingred)
print (total_count)
