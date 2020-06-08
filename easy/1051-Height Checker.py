"""
https://leetcode.com/problems/height-checker/
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.

Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.



Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0


Constraints:

1 <= heights.length <= 100
1 <= heights[i] <= 100
"""


# sort is a solution, easy to think of but not the best in terms of time and space complexity
# time complexity: O(nlogn), space complexity: O(n)

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new = list(i for i in heights)
        new.sort()
        return sum(1 for i in range(len(heights)) if new[i] != heights[i])


# this is inspired by @fan_zh in the discussion area. We don't need to sort.
# Based on the range of height and height[i], we can check if every position has the correct element.
# time complexity: O(n), space complexity: O(m), where n is the length of height and m is the largest element in height

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101
        for height in heights:
            count[height] += 1

        i = 1
        pointer = 0
        result = 0
        while i < len(count):
            if count[i] == 0:
                i += 1
            else:
                if heights[pointer] != i:
                    result += 1
                pointer += 1
                count[i] -= 1
        return result