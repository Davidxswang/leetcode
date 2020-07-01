"""
https://leetcode.com/problems/implement-trie-prefix-tree/
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""

# time complexity: O(k) for insert and O(1) for search and startswith, space complexity: O(kn) where k is the length of the word, n is the number of words inserted
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.words = set()
        self.prefix = defaultdict(set)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.add(word)
        for i in range(1, len(word)+1):
            self.prefix[word[:i]].add(word)


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return prefix in self.prefix and len(self.prefix[prefix]) != 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
