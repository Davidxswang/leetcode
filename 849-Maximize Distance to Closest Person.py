"""
https://leetcode.com/problems/maximize-distance-to-closest-person/
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left = [0] * len(seats)
        right = [0] * len(seats)
        for i in range(len(seats)):
            if seats[i] == 1:
                left[i] = 0
            elif i == 0:
                left[i] = 20000
            else:
                left[i] = left[i - 1] + 1

            if seats[~i] == 1:
                right[~i] = 0
            elif i == 0:
                right[~i] = 20000
            else:
                right[~i] = right[~i + 1] + 1

        result = 0
        for i in range(len(seats)):
            result = max(result, min(left[i], right[i]))

        return result