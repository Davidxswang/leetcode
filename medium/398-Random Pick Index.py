"""
https://leetcode.com/problems/random-pick-index/

Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""

# time complexity: O(n) for init, O(1) for pick, space complexity: O(n) where n is the length of nums

class Solution:

    def __init__(self, nums: List[int]):
        self.index = dict()
        for i, num in enumerate(nums):
            if num in self.index:
                self.index[num].append(i)
            else:
                self.index[num] = [i]

    def pick(self, target: int) -> int:
        n = len(self.index[target])
        import random
        i = random.randint(0, n-1)
        return self.index[target][i]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)