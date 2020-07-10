"""
https://leetcode.com/problems/additive-number/
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?
"""

# time complexity: O(1.6^n), space complexity: O(n). The reason why time complexity is 1.6^n is that n1+n2=n3, so len(n3) >= max(len(n1)+len(n2)), so time complexity will be 2^(effective n) = 2^(2/3 * n) = 1.6^n


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if not num:
            return True
        
        i = 0
        while i < len(num) - i - 1:
            if i > 0 and num[0] == '0':
                return False
            j = i+1
            while j < len(num) - max(i, j-i-1) - 1:
                if j > i+1 and num[i+1] == '0':
                    i += 1
                    continue
                num1 = num[0:i+1]
                num2 = num[i+1:j+1]
                add = self.add(num1, num2)
                #print(num1, num2, add)
                if num1+num2+add == num[:len(num1)+len(num2)+len(add)]:
                    if not num[len(num1)+len(num2)+len(add):] or self.isAdditiveNumber(num[len(num1):]):
                        return True
                j += 1
            i += 1
        return False
    
    def add(self, num1: str, num2: str) -> str:
        return str(int(num1) + int(num2))
        """
        
        result = ''
        addone = 0
        for i in range(0, max(len(num1), len(num2))):
            digit1 = 0 if i >= len(num1) else int(num1[~i])
            digit2 = 0 if i >= len(num2) else int(num2[~i])
            newdigit = addone + digit1 + digit2
            newdigit, addone = (newdigit, 0) if newdigit <= 9 else (newdigit - 10, 1)
            result = str(newdigit) + result
        if addone == 1:
            result = '1' + result
        return result
        """
