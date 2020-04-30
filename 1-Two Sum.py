"""
https://leetcode.com/problems/two-sum/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# this brute force method will time out in the test
# it saves memory but sacrifices time
# time complexity will be O(n^2), space complexity will be O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 1
        while True:
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                j += 1
            if j == len(nums):
                i += 1
                j = i + 1


# a better solution will be using a hash map
# it saves time but sacrifices memory
# time complexity will be O(n), space complexity will be O(n)
# be careful with the if condition and make sure it exclude itself
# another trick part is the order here, e.g. nums=[3,3], target=6
# the hashmap is actually hashmap={3:1} after one pass
# in the second pass, we use the original list nums to look up from the beginning
# so nums[0]=3 and hashmap[3]=1 make it a solution
# if we look up from the last element of nums, it will fail finding the answer
# however, this is the only case here, because there is exactly one correct answer in the list
# nums=[3,1,3], target=6 could appear in the problem set
# [2,4,1,4], target=6 will not appear in the problem set
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap and hashmap[target-nums[i]] != i:
                return [i,hashmap[target-nums[i]]]



# thanks to the solution provided by LeetCode, the time can be shorter using one-pass traverse
# it will traverse one-pass of the nums, to see if the counter-part is in the hash map, if not, save itself into it
# cannot save itself into it first and then look for the counter-part
# e.g. nums=[3,3] target=6, if we save first, hashmap={3,1} when we try to look for the counterpart of nums[1]=3,
# in this case, will cannot find the first element nums[0] in the hashmap
# time and space complexity are both O(n) because you might need to read them all and save them all in the worst case
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap:
                return [hashmap[target-nums[i]], i]
            hashmap[nums[i]] = i