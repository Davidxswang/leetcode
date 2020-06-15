"""
https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

# time complexity: O(2^n), space complexity: O(n) due to the call stack
# this is very similar to question 39, but we need to be careful with the duplicate here.

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        self.result = []
        self.recursive(candidates, 0, target, [])
        return self.result
    
    def recursive(self, candidates: List[int], start: int, target: int, temp: List[int]) -> None:
        if start > len(candidates) - 1:
            return
        if candidates[start] > target:
            self.recursive(candidates, start+1, target, [])
        else:
            total = sum(temp) + candidates[start]
            if total == target:
                self.result.append(temp+[candidates[start]])
                # in this case, we need to try another distinct element, because if we try the same element, we will get the same result -> duplicate
                start += 1
                while start < len(candidates) and candidates[start] == candidates[start-1]:
                    start += 1
                self.recursive(candidates, start, target, temp)
            elif total < target:
                self.recursive(candidates, start+1, target, temp+[candidates[start]])
                # in this case, we need to try another distinct number, because if we don't add the current element into the temp, but we move to the same element as current one, it will execute the last line of code, which will add the same element to the temp again. So we should try either add this element in the temp or not add the same element in the temp.
                start += 1
                while start < len(candidates) and candidates[start] == candidates[start-1]:
                    start += 1
                self.recursive(candidates, start, target, temp)
            else:
                self.recursive(candidates, start+1, target, temp)
