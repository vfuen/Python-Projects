import json

load_numbers = 'numbers01.json'

with open(load_numbers) as ln:
    numbers01 = json.load(ln)

print(numbers01)