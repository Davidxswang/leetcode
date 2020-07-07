"""
https://leetcode.com/problems/h-index-ii/
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
"""

# time complexity: O(logn), space complexity: O(logn)
# this is very similar to H-index I, the difference here is we don't need to sort them anymore.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        result = 0
        
        def helper(start, end):
            nonlocal result
            if start > end:
                return
            
            mid = start + (end-start) // 2
            if len(citations)-mid >= citations[mid]:
                result = max(result, citations[mid])
                helper(mid+1, end)
            else:
                result = max(result, len(citations)-mid)
                helper(start, mid-1)
        
        helper(0, len(citations)-1)
        
        return result
