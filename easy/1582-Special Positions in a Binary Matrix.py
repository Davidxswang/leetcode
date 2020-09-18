"""
https://leetcode.com/problems/special-positions-in-a-binary-matrix/
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

 

Example 1:

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:

Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions. 
Example 3:

Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2
Example 4:

Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3
 

Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is 0 or 1.
"""

# time complexity: O(row*column), space complexity: O(column)

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        columns = set()
        
        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                column = mat[i].index(1)
                if column not in columns and column-200 not in columns:
                    columns.add(column)
                elif column in columns:
                    columns.remove(column)
                    columns.add(column-200)
        
        result = 0
        for column in columns:
            if column >= 0:
                found = 0
                for row in range(len(mat)):
                    if mat[row][column] == 1:
                        found += 1
                        if found > 1:
                            break
                if found == 1:
                    result += 1
        
        return result
