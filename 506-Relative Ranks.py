"""
https://leetcode.com/problems/relative-ranks/
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""

# time complexity: O(nlogn), space complexity: O(1)
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        self.sort(nums, 0, len(nums) - 1)
        result = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                result[nums[i][1]] = 'Gold Medal'
            elif i == len(nums) - 2:
                result[nums[i][1]] = 'Silver Medal'
            elif i == len(nums) - 3:
                result[nums[i][1]] = 'Bronze Medal'
            else:
                result[nums[i][1]] = str(len(nums) - i)
        return result

    def sort(self, nums: List[int], start: int, end: int) -> None:
        if start >= end:
            return
        import random
        pivot = random.randrange(start, end + 1)
        nums[pivot], nums[start] = nums[start], nums[pivot]
        i = j = start + 1
        while j <= end:
            if nums[j][0] < nums[start][0]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        nums[start], nums[i - 1] = nums[i - 1], nums[start]
        self.sort(nums, start, i - 2)
        self.sort(nums, i, end)
