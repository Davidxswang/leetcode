"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

# My version. To put every element to where it should locate.
# time complexity: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i <= len(nums)-1:
            if nums[i] is None:
                i += 1
                continue
            if nums[i] != i+1:
                temp = nums[i]
                if nums[temp-1] == temp:
                    nums[i] = None
                    i += 1
                else:
                    nums[i], nums[temp-1] = nums[temp-1], nums[i]
            else:
                i += 1
        i = 0
        while i <= len(nums)-1:
            if nums[i] is None:
                result.append(i+1)
            i += 1
        return result

# I found in the dicussion area that @leetcodeftw had a very brilliant solution.
# This use the property that 1 <= a[i] <= n in the problem set, which is very genius.
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]