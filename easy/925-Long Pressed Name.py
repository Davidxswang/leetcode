"""
https://leetcode.com/problems/long-pressed-name/
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
The characters of name and typed are lowercase letters.
"""

# time complexity: O(m+n), space complexity: O(1)

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    return False
                else:
                    if typed[j] == typed[j - 1]:
                        j += 1
                    else:
                        return False

        if i >= len(name):
            if j >= len(typed):
                return True
            else:
                while j < len(typed):
                    if typed[j] != name[-1]:
                        return False
                    j += 1
                return True
        return False
