"""
https://leetcode.com/problems/largest-triangle-area/
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""

# time complexity: O(n^3), space complexity: O(1)

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        self.points = points
        self.area = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    lenij = self.getLength(i, j)
                    lenik = self.getLength(i, k)
                    lenjk = self.getLength(j, k)
                    if abs(lenij - lenik) < lenjk < (lenij + lenik):
                        self.updateArea(lenij, lenik, lenjk)

        return self.area

    def getLength(self, i: int, j: int) -> float:
        import math
        return math.sqrt((self.points[i][0] - self.points[j][0]) ** 2 + (self.points[i][1] - self.points[j][1]) ** 2)

    def updateArea(self, l1: float, l2: float, l3: float) -> None:
        s = (l1 + l2 + l3) / 2
        area = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
        self.area = max(self.area, area)