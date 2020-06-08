"""
https://leetcode.com/problems/image-smoother/
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""

# time complexity: O(mn), space complexity: O(1) (result space omitted), where m and n are the width and length of M

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(M)):
            result.append([])
            for j in range(len(M[0])):
                sur = [M[row][col] for row in range(max(0,i-1), min(len(M),i+2))
                                   for col in range(max(0,j-1), min(len(M[0]),j+2))]
                result[i].append(int(sum(sur)/len(sur)))
        return result