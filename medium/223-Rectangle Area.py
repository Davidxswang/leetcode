"""
https://leetcode.com/problems/rectangle-area/
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.
"""

# time complexity: O(1), space complexity: O(1)

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = abs(C-A) * abs(D-B)
        area2 = abs(G-E) * abs(H-F)
        # see if there is any intersection
        left = max(A, E)
        right = min(C, G)
        up = min(D, H)
        down = max(B, F)
        if left < right and up > down:
            intersection = abs(right-left) * abs(up-down)
        else:
            intersection = 0
        return area1 + area2 - intersection
