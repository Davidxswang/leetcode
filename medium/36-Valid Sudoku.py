"""
https://leetcode.com/problems/valid-sudoku/
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

# time complexity: O(n^2), space complexity: O(n), where n is the length of the board

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            check = [0] * 9
            for column in range(9):
                if board[row][column] == '.':
                    continue
                n = ord(board[row][column]) - ord('1')
                if check[n] == 1:
                    return False
                check[n] += 1
        
        for column in range(9):
            check = [0] * 9
            for row in range(9):
                if board[row][column] == '.':
                    continue
                n = ord(board[row][column]) - ord('1')
                if check[n] == 1:
                    return False
                check[n] += 1
        
        for start_row in range(0, 9, 3):
            for start_column in range(0, 9, 3):
                check = [0] * 9
                for row in range(start_row, start_row+3):
                    for column in range(start_column, start_column+3):
                        if board[row][column] == '.':
                            continue
                        n = ord(board[row][column]) - ord('1')
                        if check[n] == 1:
                            return False
                        check[n] += 1
        
        return True
