"""
https://leetcode.com/problems/lru-cache/
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

# two methods are provided, both of them are inspired by @tusizi in the discussion
# The first is using ordered list provided by python collections package
# The second is using double linked list and dictionary. The double linked list is for storing the order, the dictionary is for storing the key-node mapping.
# time complexity: O(1) for both, space complexity: O(n), second uses more space compared with the first one.

class LRUCache:
    
    """
    this solution is using ordered dict
    
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if self.capacity == len(self.cache):
                self.cache.popitem(last=False)
            self.cache[key] = value     
    """
    
    
    """
    another solution will be using a double linked list and a dict, dict is used to store the key-value, and double linked list is to keep the ordering
    """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()     # key => Node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del self.cache[node.key]
        
    def _add(self, key, val):
        node = Node(key, val)
        self.tail.prev.next, self.tail.prev, node.prev, node.next = node, node, self.tail.prev, self.tail
        self.cache[key] = node
        
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            key, val = node.key, node.val
            self._delete(node)
            self._add(key, val)
            return val
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
            self._add(key, value)
        else:
            if len(self.cache) == self.capacity:
                self._delete(self.head.next)
            self._add(key, value)
        
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
