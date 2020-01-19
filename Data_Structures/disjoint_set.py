child_parent = {
    'a': 'a',
    'b': 'b',
    'c': 'c',
    'd': 'd',
    'e': 'e',
    'f': 'f',
    'g': 'g',
    'h': 'h',
    'i': 'i',
}


def find(r):
    print('Calling for :', r)
    if child_parent[r] == r:
        return r
    else:
        child_parent[r] = find(child_parent[r])
        return child_parent[r]


# return find(child_parent[r])


def union(a, b):
    # here b is parent and a is child of b
    u = find(a)
    v = find(b)
    if u == v:
        print("They are already friends")
    else:
        child_parent[u] = v  # Or you can write par[v]=u too


union('b', 'a')
print(child_parent)
union('c', 'b')
print(child_parent)
union('i', 'h')
print(child_parent)
union('g', 'h')
print(child_parent)
union('b', 'a')
print(child_parent)
union('e', 'f')
print(child_parent)
union('f', 'h')
print(child_parent)
union('d', 'e')
print(child_parent)
union('h', 'a')
print(child_parent)
find('f')
