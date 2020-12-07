import sys

data = [line.rstrip() for line in sys.stdin.readlines()]
rules = [line.split(' bags contain ') for line in data]

allowed_containers = set()
def find_containers(type):
  result = []
  for rule in rules:
    if type in rule[1]:
      result.append(rule[0])
  return result

def add_containers(containers):
  for container in containers:
    if container not in allowed_containers:
      allowed_containers.add(container)
      add_containers(find_containers(container))

add_containers(['shiny gold'])
print (len(allowed_containers)-1)
