"""
https://leetcode.com/problems/next-permutation/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

# time complexity: O(n), space complexity: O(1)
# I didn't come up with this solution. This is inspired by @yuyibestman in the discussion area. 
# In the Wikipedia, it says this method actually came from Narayana Pandita in 14th century India. The method is:
#   1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
#   2. Find the largest index l greater than k such that a[k] < a[l].
#   3. Swap the value of a[k] with that of a[l].
#   4. Reverse the sequence from a[k + 1] up to and including the final element a[n].

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        # a decending ordered list cannot be larger, so we need to find the first ascending order pair.
        # the only way to make a number larger is to make a small number larger, to do this, we have to find a digit that can be larger
        # to make the result smallest, we should search from the right.
        pos = None
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                pos = i
                break
        if pos is None:
            nums.reverse()
            return
        
        # now we need to make the nums[pos] larger, but we cannot just find a larger number and replace nums[pos] by it because we need to make the result as small as possible. So we need to find the number that is larger than nums[pos] but it's the smallest on the right of nums[pos]
        for i in range(len(nums)-1, pos, -1):
            if nums[i] > nums[pos]:
                nums[pos], nums[i] = nums[i], nums[pos]
                break
                
        # now we have make the number larger but the problem is that this is not the smallest result
        # because the number to the right of nums[pos] is a decending ordered list. We have to make it a ascending ordered list to make it smallest possible result
        i = pos + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        
