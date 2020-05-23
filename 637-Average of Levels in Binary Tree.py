"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""

# time complexity: O(n), space complexity: O(width of the tree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        result = []
        levelnumber = 1
        scannumber = 0
        number = 0
        levelsum = 0
        while queue:
            element = queue.pop(0)
            scannumber += 1
            if element is not None:
                number += 1
                levelsum += element.val
                queue.append(element.left)
                queue.append(element.right)
            if scannumber == levelnumber:
                if number == 0:
                    return result
                else:
                    result.append(levelsum/number)
                scannumber = 0
                levelnumber = len(queue)
                number = 0
                levelsum = 0
        return result