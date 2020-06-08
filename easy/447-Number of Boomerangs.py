"""
https://leetcode.com/problems/number-of-boomerangs/
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""

# Thanks to the help from @Devanshi in discussion area.
# A hash list is used to store the distances from each point to every other points.
# Since only the sum number matters, we can just use the hash list to calculate the number of tuples.
# time complexity: O(n^2), space complexity: O(n), where n is the length of the array points
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)):
            dis = {}
            for j in range(len(points)):
                if j == i:
                    continue
                else:
                    distance = self.distance2(points[i], points[j])
                    if distance in dis:
                        dis[distance] += 1
                    else:
                        dis[distance] = 1
            values = dis.values()
            result += sum([i * (i - 1) for i in values])
        return result

    def distance2(self, point1: List[int], point2: List[int]) -> int:
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2