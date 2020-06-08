"""
https://leetcode.com/problems/path-sum-iii/
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""

# This is inspired by @wonderlives in discussion area.
# time complexity: O(n^2), space complexity: O(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0
        self.dfs(root, sum)
        return self.result

    def dfs(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.test(root, sum)

    def test(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return
        if root.val == sum:
            self.result += 1

        self.test(root.left, sum - root.val)
        self.test(root.right, sum - root.val)


# This is another solution inspired by @wonderlives in discussion area.
# time complexity: O(n), space complexity: O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.result = 0
        cache = {0: 1}
        self.dfs(root, sum, 0, cache)
        return self.result

    def dfs(self, root: TreeNode, sum: int, currentPathSum: int, cache: dict):
        if root is None:
            return
        currentPathSum += root.val
        oldPathSum = currentPathSum - sum
        self.result += cache.get(oldPathSum, 0)
        cache[currentPathSum] = cache.get(currentPathSum, 0) + 1
        self.dfs(root.left, sum, currentPathSum, cache)
        self.dfs(root.right, sum, currentPathSum, cache)
        cache[currentPathSum] -= 1