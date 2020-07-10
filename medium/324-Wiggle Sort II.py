"""
https://leetcode.com/problems/wiggle-sort-ii/

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?
"""

# time complexity: O(nlogn), space complexity: O(1)
# the solution is inspired by @StefanPochmann and @huoshankou in the discussion area.
# the key here is actually the process of rewiring the index.
# by (2*i+1) % (n | 1), we can rewire the index from 0,1,2,3,4,5 to 1,3,5,0,2,4 and from 0,1,2,3,4 to 1,3,0,2,4
 


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        
        def newIndex(i):
            # if len(nums) is odd, then 2i+1 % n, e.g. n=5, 0,1,2,3,4 ==2i+1==> 1,3,5,7,9 ==%n==> 1,3,0,2,4 ==> so the first two will be mapped to the even positions where large(>median) numbers are
            # if len(nums) is even, then 2i+1 % (n+1), e.g. n=6, 0,1,2,3,4,5 ==2i+1==> 1,3,5,7,9,11 ==%(n+1)==> 1,3,5,0,2,4 ==> so the first three will be mapped to the even positions where large(>median) numbers are
            return (2*i+1) % (len(nums) | 1)
        
	# cannot use this method, because in theory, the time complexity of finding the k-th largest element in an array using quick sort is O(n) on average, but the last test case, it's an extreme case where using quick sort will not shrink the search range into half. Instead, it will shrink only 1 or 2 or 10 every time, which is very small compared with the size of the input, which is around 60000.
	# using quick sort in this case will approach n^2, while sorting it completely only takes O(nlogn) time complexity using built-in sort method.

        # median = self.findKthLargest(nums, (len(nums)+1)//2)
        # print(nums, median, nums[(len(nums)+1)//2-1])
        
        nums.sort(reverse=True)
        median = nums[len(nums) // 2]
        
        left, i, right = 0, 0, len(nums)-1
        while i <= right:
            left_index = newIndex(left)
            i_index = newIndex(i)
            right_index = newIndex(right)
            if nums[i_index] < median:
                nums[i_index], nums[right_index] = nums[right_index], nums[i_index]
                right -= 1
            elif nums[i_index] > median:
                nums[i_index], nums[left_index] = nums[left_index], nums[i_index]
                i += 1
                left += 1
            else:
                i += 1
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
	# I have changed the code here, it's not quick sort but still it cannot deal with the last test case
        def helper(arr, startIdx, endIdx, n):
            while True:
                #print(startIdx, endIdx)
                pivot = startIdx
                leftIdx = startIdx + 1
                rightIdx = endIdx
                while leftIdx <= rightIdx:
                    if arr[pivot] < arr[leftIdx] and arr[pivot] > arr[rightIdx]:
                        arr[leftIdx], arr[rightIdx] = arr[rightIdx], arr[leftIdx]
                    if arr[pivot] >= arr[leftIdx]:
                        leftIdx += 1
                    if arr[pivot] <= arr[rightIdx]:
                        rightIdx -= 1
                arr[pivot], arr[rightIdx] = arr[rightIdx], arr[pivot]

                if rightIdx == n:
                    return arr[rightIdx]
                elif n > rightIdx:
                    startIdx = rightIdx + 1
                else:
                    endIdx = rightIdx - 1
                    
        n = len(nums) - k
        return helper(nums, 0, len(nums)-1, n)
