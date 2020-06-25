"""
https://leetcode.com/problems/restore-ip-addresses/
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single points.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""

# time complexity: O(1), space complexity: O(1)
# here, we should only process those strings that are less than or equal to 12 digits, so the time complexity and space complexity is contant order

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        self.result = []
        self.s = s
        self.recursive([], 0)
        return self.result
    
    def recursive(self, temp: List[str], start: int) -> None:
        if start == len(self.s) and len(temp) == 4:
            self.result.append('.'.join(temp))
            return
        elif start == len(self.s) and len(temp) != 4:
            return
        elif start > len(self.s):
            return
        
        for i in range(1, 4):
            if i == 1:
                self.recursive(temp+[self.s[start:start+i]], start+i)
            elif i == 2 and 10 <= int(self.s[start:start+i]) <= 99:
                self.recursive(temp+[self.s[start:start+i]], start+i)
            elif i == 3 and 100 <= int(self.s[start:start+i]) <= 255:
                self.recursive(temp+[self.s[start:start+i]], start+i)
