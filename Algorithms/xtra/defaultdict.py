from collections import defaultdict

dict = defaultdict(list)
dict['python'].append('is_awesome')
dict['python'].append('is_super')

for i in dict:
    print(dict)

food_count = defaultdict(int)
item = "i am sharif i am simple man sharif man"
item = item.split()
print(item)
for i in item:
    food_count[i] += 1

print(food_count)
print(*food_count.values())
