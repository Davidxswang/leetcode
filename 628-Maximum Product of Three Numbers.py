"""
https://leetcode.com/problems/maximum-product-of-three-numbers/
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6


Example 2:

Input: [1,2,3,4]
Output: 24


Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

# I didn't come up with a clean solution in O(n), thanks to the solution provided by the questions.
# The maximum happens in such three situations:
# 1. maximum < 0. In this case, we should find the maximal 3 numbers to make the product maximum.
# 2. maximum = 0. In this case, we can find 0 and another 2 negative numbers to make the product = 0, which is largest.
# 3. maximum > 0. In this case, we can find the maximum by max[0]*max[1]*max[2] or max*min[0]*min[1] whichever is larger.

# time complexity: O(n), space complexity: O(1)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1 = min2 = pow(2, 31) + 1
        max1 = max2 = max3 = -pow(2, 31) - 1
        # min1 < min2
        # max1 < max2 < max3
        for i in range(len(nums)):
            if nums[i] < min1:
                min1, min2 = nums[i], min1
            elif nums[i] < min2:
                min2 = nums[i]

            if nums[i] > max3:
                max1, max2, max3 = max2, max3, nums[i]
            elif nums[i] > max2:
                max1, max2 = max2, nums[i]
            elif nums[i] > max1:
                max1 = nums[i]

        return max(min1 * min2 * max3, max1 * max2 * max3)