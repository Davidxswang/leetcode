"""
https://leetcode.com/problems/container-with-most-water/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

  
Example:

  Input: [1,8,6,2,5,4,8,3,7]
  Output: 49
  """

# time complexity: O(n), space complexity: O(1)
# this is very interesting problem. I got the inspiration from the problem solution.
# We just start from the beginning and the end, move one pointer each time.
# Each time we will move a shorter one, because only the shorter one decideds the current volume, only by changing the shorter one, can a difference be made.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The reason why we need to move the shorter line towards the center is that only changing the shortline can change the area, moving the longer line cannot change the current area, i.e. the area depends on the shorter line.
        """
        i = 0
        j = len(height)-1
        result = 0
        while i < j:
            result = max(result, (j-i)*min(height[i],height[j]))
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return result
