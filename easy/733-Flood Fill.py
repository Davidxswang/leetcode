"""
https://leetcode.com/problems/flood-fill/
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""

# time complexity: O(mn), space complexity: O(mn), where m and n are the height and width of image

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.result = []
        self.image = image
        self.newColor = newColor
        self.oldColor = image[sr][sc]
        for i in range(len(self.image)):
            self.result.append([])
            for j in range(len(self.image[0])):
                self.result[i].append(self.image[i][j])
        self.fill(sr, sc)
        return self.result

    def fill(self, row: int, column: int) -> None:
        if self.image[row][column] == self.oldColor:
            self.image[row][column] = -1
            self.result[row][column] = self.newColor
            for r in range(row - 1, row + 2, 2):
                if r < 0 or r > len(self.image) - 1 or self.image[r][column] == -1 or self.image[r][
                    column] != self.oldColor:
                    pass
                else:
                    self.fill(r, column)
            for c in range(column - 1, column + 2, 2):
                if c < 0 or c > len(self.image[0]) - 1 or self.image[row][c] == -1 or self.image[row][
                    c] != self.oldColor:
                    pass
                else:
                    self.fill(row, c)