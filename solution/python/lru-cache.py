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

class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
    
class DLL:    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def __str__(self):
        op = ""
        curr_node = self.head.next
        
        while curr_node != None:
            # print(curr_node, curr_node.val)
            op += str(curr_node.key) + " -> "
            curr_node = curr_node.next
            
            if curr_node == self.tail:
                op = op.rstrip("-> ")
                break
        
        return op
   
    
    def push_front(self, new_node):

        print("Before pushfront:", self)

        if new_node.next != None and new_node.prev != None:
            new_node.prev.next = new_node.next
            new_node.next.prev = new_node.prev

        new_node.prev = self.head
        new_node.next = self.head.next
        
        new_node.next.prev = new_node
        self.head.next = new_node

        print("After pushfront:", self)
        
    def pop_back(self):

        print("Before popback:", self)

        last_node = self.tail.prev

        last_node.prev.next = self.tail
        self.tail.prev = last_node.prev

        
        print("After popback:", self)

        return last_node

    def delete_node(self, node):

        print("Deleting node:", node.val)

        node.prev.next = node.next
        node.next.prev = node.prev

        print("After deleting:", self)
        
   
    

class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = DLL()
        self.capacity = capacity
        self.size = 0

        self.map = dict()
        
     
    def get(self, key: int) -> int:
        
        print("Getting :", key)
        
        if key in self.map:
            # print("Before getting:", self.lru_cache)
            # print("Got value :", self.map[key].val)
            self.lru_cache.push_front(self.map[key])
            print("After getting:", self.lru_cache)
            return self.map[key].val
        else:
            print("Not found.")
            return -1
        
        
            

    def put(self, key: int, value: int) -> None:
        
        print("Inserting :", key, value)
        
        if self.size < self.capacity and key not in self.map:    
            print("Size:", self.size)
            self.size += 1
        else:
            if key not in self.map:
                popped_node = self.lru_cache.pop_back()
                self.map.pop(popped_node.key, None)
            else:
                self.lru_cache.delete_node(self.map[key])
            
        new_node = Node(key, value)
        self.lru_cache.push_front(new_node)
        self.map[key] = new_node
        
        print("After insertion:", self.lru_cache)
    
        

def process_list(l):
    lru_cache = LRUCache(l.pop(0)[0])

    for entry in l:
        if len(entry) == 1:
            lru_cache.get(entry[0])
        else:
            lru_cache.put(entry[0], entry[1])
        
def main():
    
    process_list([[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]])

if __name__ == "__main__":
    main()