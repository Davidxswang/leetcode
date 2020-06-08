"""
https://leetcode.com/problems/third-maximum-number/
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


# time complexity: O(n), space complexity: O(1)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxlist = [None, None, None]
        for i in range(3):
            for j in range(len(nums)):
                if maxlist[i] is None:
                    if i == 0:
                        maxlist[i] = nums[j]
                    else:
                        if nums[j] < maxlist[i-1]:
                            maxlist[i] = nums[j]
                else:
                    if nums[j] > maxlist[i]:
                        if i == 0:
                            maxlist[i] = nums[j]
                        else:
                            if nums[j] < maxlist[i-1]:
                                maxlist[i] = nums[j]
            if maxlist[i] is None:
                break
        if maxlist[-1] is not None:
            return maxlist[-1]
        else:
            return maxlist[0]

# Using divide and conquer based on quicksort
# time complexity: O(n), space complexity: O(1)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = list(set(nums))
        if len(s) == 1:
            return s[0]
        if len(s) == 2:
            return s[0] if s[0] > s[1] else s[1]
        return self.findthirdmax(s, 0, len(s) - 1, 3)

    def findthirdmax(self, nums: List[int], start: int, end: int, position: int) -> int:
        import random
        pivot = random.randrange(start, end + 1)
        nums[start], nums[pivot] = nums[pivot], nums[start]
        i = start + 1
        j = start + 1
        while j <= end:
            if nums[j] > nums[start]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            else:
                j += 1
        nums[i - 1], nums[start] = nums[start], nums[i - 1]
        if i - 1 - start == position - 1:
            return nums[i - 1]
        else:
            if i - start > position:
                return self.findthirdmax(nums, start, i - 2, position)
            if i - start < position:
                return self.findthirdmax(nums, i, end, position - (i - start))