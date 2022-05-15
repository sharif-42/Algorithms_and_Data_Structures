from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.table = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if key in self.table:
            self.q.remove(key)
            self.q.append(key)
            return self.table[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.q.remove(key)
        if len(self.q) == self.cap:
            del self.table[self.q.popleft()]
        self.q.append(key)
        self.table[key] = value


if __name__ == "__main__":
    lru_cache = LRUCache(capacity=2)
    lru_cache.put(1, 0)
    print('cache after put(1,0)', lru_cache.table)
    lru_cache.put(2, 2)
    print('cache after put(2,2)', lru_cache.table)
    print(lru_cache.get(1))
    print(lru_cache.q)
    lru_cache.put(3, 3)
    print('cache after put(3,3)', lru_cache.table)
    print(lru_cache.get(2))
    print(lru_cache.q)

    lru_cache.put(4, 4)
    print('cache after put(4,4)', lru_cache.table)
    print(lru_cache.get(1))
    print(lru_cache.q)

    print(lru_cache.get(3))
    print(lru_cache.get(4))

    # lru_cache = LRUCache(capacity=1)
    # lru_cache.put(2, 1)
    # print('cache after put(2,1)', lru_cache.cache)
    # print('recently used', lru_cache.get(2))
    #
    # lru_cache.put(3,2)
    # print('cache after put(3,2)', lru_cache.cache)
    #
    # print('recently used', lru_cache.get(2))
    # print('recently used', lru_cache.get(3))

    # lru_cache = LRUCache(capacity=2)
    # print(lru_cache.get(2))
    #
    # lru_cache.put(2, 6)
    # print('cache after put(2,6)', lru_cache.cache)
    # print(lru_cache.get(1))
    #
    # lru_cache.put(1, 5)
    # print('cache after put(1,5)', lru_cache.cache)
    #
    # lru_cache.put(1, 2)
    # print('cache after put(1,2)', lru_cache.cache)
    # print(lru_cache.get(1))
    # print(lru_cache.get(2))

    # lru_cache = LRUCache(capacity=2)
    # lru_cache.put(2, 1)
    # print('cache after put(2,1)', lru_cache.cache)
    #
    # lru_cache.put(1, 1)
    # print('cache after put(1,1)', lru_cache.cache)
    #
    # lru_cache.put(2, 3)
    # print('cache after put(2,3)', lru_cache.cache)
    #
    # lru_cache.put(4, 1)
    # print('cache after put(4,1)', lru_cache.cache)
    #
    # print(lru_cache.get(1))
    # print(lru_cache.get(2))



