"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""

# time complexity: O(length of the word), space complexity: O(total number of letters in the inserted words)
# the key is to build a tree using Trie structure. If we meet a '.' in the expression, we need to search all the children, if we reach the end of the search key, we need to check if this is the end of a word.
# this solution is inspired by @caikehe in the discussion area. https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/59725/Python-easy-to-follow-solution-using-Trie.

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for letter in word:
            node = node.children[letter]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.dfs(self.root, word)
    
    def dfs(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.isWord
        if word[0] == '.':
            for child in node.children.values():
                if self.dfs(child, word[1:]):
                    return True
            return False
        else:
            if word[0] not in node.children:
                return False
            return self.dfs(node.children[word[0]], word[1:])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
