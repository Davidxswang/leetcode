"""
https://leetcode.com/problems/count-binary-substrings/
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""

# time complexity: O(n), space complexity: O(n)

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        lengths = list()
        i = 0
        temp = 0
        while i < len(s):
            if i == len(s) - 1 or i != len(s) - 1 and s[i] != s[i + 1]:
                lengths.append(temp + 1)
                temp = 0
            else:
                temp += 1
            i += 1

        result = 0
        for i in range(len(lengths) - 1):
            result += min(lengths[i], lengths[i + 1])

        return result


# I just found a very concise implementation proposed by the solution of this problem set.
# Very beautiful.
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))


# This is the second solution provided by the solution of this problem.
# It's very interesting, but tricky here as the answer need to add min(prev, curr)
# because when we finish calculating the last one, we either ends up with prev, curr = curr, 1 when nums[last] != nums[last-1]
# or ends up with curr += 1
# No matter which case we ends up with, we need to calculate the last prev and curr anyway.

# time complexity: O(n), space complexity: O(1)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer = 0
        prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                answer += min(curr, prev)
                prev, curr = curr, 1
            else:
                curr += 1

        return answer + min(prev, curr)