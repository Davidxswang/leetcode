"""
https://leetcode.com/problems/h-index/
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""

# time complexity: O(n), space complexity: O(logn)
# this is very similar to the find the k-th largest number in the array except that we need a variable here to remember the best possible result we have seen.

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        self.result = 0
        self.find(citations, 0, len(citations)-1)
        return self.result
    
    def find(self, citations: List[int], start: int, end: int) -> None:
        if start > end:
            return
        import random
        pivot = random.randrange(start, end+1)
        citations[pivot], citations[start] = citations[start], citations[pivot]
        i = j = start + 1
        while j <= end:
            if citations[j] >= citations[start]:
                citations[j], citations[i] = citations[i], citations[j]
                i += 1
            j += 1
        citations[start], citations[i-1] = citations[i-1], citations[start]
        if citations[i-1] == i:
            self.result = max(self.result, i)
            self.find(citations, start, i-2)
        elif citations[i-1] < i:
            self.result = max(self.result, citations[i-1])
            self.find(citations, start, i-2)
        else:
            self.result = max(self.result, i)
            self.find(citations, i, end)
