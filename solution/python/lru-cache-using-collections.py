"""
LRU Cache

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
    * LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    * int get(int key) Return the value of the key if the key exists, otherwise return -1.
    * void put(int key, int value) Update the value of the key if the key exists. 
      Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Follow up:
    Could you do get and put in O(1) time complexity?

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
    1 <= capacity <= 3000
    0 <= key <= 3000
    0 <= value <= 10^4
    At most 3 * 10^4 calls will be made to get and put.

"""

from collections import OrderedDict

class LRUCache:

    lru_cache = OrderedDict()
    lru_size = 0
    current_size = 0
    
    def __init__(self, capacity: int):
        self.lru_size = capacity
        # print("Initialized : ", self.lru_cache)
        # print("Capacity:", self.lru_size)
        
        self.lru_cache.clear()
            
        # print("After clearing:", self.lru_cache)

    def get(self, key: int) -> int:
        if key in self.lru_cache:
            value = self.lru_cache[key]
            self.lru_cache.pop(key)
            self.lru_cache[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        # print("Inserting:", value)
        
        if key in self.lru_cache:
            self.lru_cache.pop(key)
            self.lru_cache[key] = value
        else:
            if self.current_size < self.lru_size:
                self.lru_cache[key] = value
                self.current_size += 1
            else:
                self.lru_cache.popitem(last=False)
                self.lru_cache[key] = value
        
        # print("After inserting:", self.lru_cache)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)