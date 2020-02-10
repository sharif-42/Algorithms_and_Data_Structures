"""
Find Which Multiple Elements on a list
"""

# Using Set
lst = [1, 2, 3, 4, 5, 6, 1, 2, 10, 1]
lst2 = list(set(lst))
for i in lst2:
    if i in lst:
        lst.remove(i)
print("Multiple Elements: ", lst)

# how to find all multiple element in a list with their index
list = ['foo', 'spam', 'egg', 'foo']
for i in list:
    foo_indexes = [n + 1 for n, x in enumerate(list) if x == i]
    print(i, len(foo_indexes), foo_indexes)
