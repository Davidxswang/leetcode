"""
https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


# The first solution is given by me, which is very slow and needs a lot of spaces because a lot of spaces are left empty. 
# time complexity: O(n), space complexity: O(n)
# The second solution is inspired by @notfresh in the discussion area.
# He gave a very good explanation under the post of @pharrellyhy: we should think of zigzag as a way of reading letters and distribute them to different bucket.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        slow way
        result = []
        i = 0
        counter = 0
        increasing = True
        while counter < len(s):
            if i == 0:
                result.append(['']*numRows)
                result[-1][i] = s[counter]
                i = (i+1) % numRows
                counter += 1
                increasing = True
            elif i == numRows - 1:
                result[-1][i] = s[counter]
                increasing = False
                i -= 1
                counter += 1
            elif increasing:
                result[-1][i] = s[counter]
                i += 1
                counter += 1
            else:
                result.append(['']*numRows)
                result[-1][i] = s[counter]
                i -= 1
                counter += 1
        ret = ''
        for i in range(numRows):
            for j in range(len(result)):
                if result[j][i] != '':
                    ret += result[j][i]
        return ret
        """
        if numRows == 1 or numRows >= len(s):
            return s
        buckets = [''] * numRows
        bucket_number = 0
        for letter in s:
            buckets[bucket_number] += letter
            if bucket_number == 0:
                increment = 1
            elif bucket_number == numRows - 1:
                increment = -1
            bucket_number += increment
        return ''.join(buckets)
