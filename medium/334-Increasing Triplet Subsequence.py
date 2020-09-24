"""
https://leetcode.com/problems/increasing-triplet-subsequence/
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""

# time complexity: O(n), space complexity: O(1)
# the solution is provided by @girikuncoro in the discussion area.
# smallest_first is the smallest value till the current number
# smallest_second is the smallest value2 in (value1, value2) pair, which mean this is at least one pair ending with value2
# if there is any value large than smallest_second then an increasing triplet (value1, value2, value3) exists.

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest_first = smallest_second = float('inf')
        
        for n in nums:
            if n <= smallest_first:
                smallest_first = n
            elif n <= smallest_second:
                smallest_second = n
            else:
                return True
        
        return False