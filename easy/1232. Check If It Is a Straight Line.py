"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        if coordinates[1][0] == coordinates[0][0]:
            vertical = True
        else:
            vertical = False
            k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(1, len(coordinates)-1):
            if vertical and coordinates[i+1][0] == coordinates[i][0] or not vertical and coordinates[i+1][0] != coordinates[i][0] and k == (coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0]):
                continue
            else:
                return False
        return True
