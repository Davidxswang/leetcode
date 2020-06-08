"""
https://leetcode.com/problems/design-hashset/
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

# time complexity: O(1), space complexity: O(n)

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = list([] for i in range(1000))

    def _getHash(self, key: int) -> int:
        return int(str(hash(str(key)))[-3:])

    def add(self, key: int) -> None:
        index = self._getHash(key)
        for i in self.bucket[index]:
            if i == key:
                return
        self.bucket[index].append(key)

    def remove(self, key: int) -> None:
        index = self._getHash(key)
        for i in self.bucket[index]:
            if i == key:
                self.bucket[index].remove(i)
                return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self._getHash(key)
        for i in self.bucket[index]:
            if i == key:
                return True
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)