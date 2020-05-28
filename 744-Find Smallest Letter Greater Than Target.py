"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"
Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0]:
            return letters[0]
        elif target >= letters[-1]:
            return letters[0]
        else:
            # letter[0] <= target < letter[-1]
            for i in range(len(letters) - 1):
                if letters[i] <= target < letters[i + 1]:
                    return letters[i + 1]
