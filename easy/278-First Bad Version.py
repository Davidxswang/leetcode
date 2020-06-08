"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

# The tricky part here is the case start == end.
# time complexity: O(logn), space complexity: O(logn) due to the function call stack
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.check(1, n)

    def check(self, start: int, end: int) -> int:
        if start == end:
            return start
        middle = start + (end - start) // 2
        middleResult = isBadVersion(middle)
        if middleResult:
            return self.check(start, middle)
        else:
            middle1Result = isBadVersion(middle + 1)
            if middle1Result:
                return middle + 1
            else:
                return self.check(middle + 1, end)