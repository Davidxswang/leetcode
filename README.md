# What is this?
I decided to walk through the LeetCode problems 5/day, and publish some of the solutions here. Hopefully it will be helpful for myself or some of you in front of the screen.

# Some very interesting problems
## 28 Implement strStr()
KMP pattern search algorithm use a O(m+n) time complexity to search a substring in a string, which is really incredible. The key actually is to make use of the information embedded in the pattern string.

## 53 Maximum Subarray()
### Divide and Conquer
Every time, it divides the array into two parts, calculates the maximum subarray in each part(left and right), and the array that is across the middle element. Max(left sum, right sum, the sum across the middle element) is the result of that level.
### Dynamic Programming
Kadane's algorithm uses the assumption that whenever I evaluate a new element nums[i] and check if I should connect it to a already-found subarray previously to make a contiguous subarray, the previous part should not lower the current value nums[i]. Otherwise I should start from nums[i] + 0 instead of nums[i] + Negative Value.

## 371 Sum of Two Integers
When solving this problem, I found the post that @LHearen wrote was very useful, so I suggest that every one who is working on LeetCode take a look at this post: https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently

## 437 Path Sum III
Given a binary tree, find the number of paths that sum to a given value. The path can start and end anywhere as long as start -> end is parent -> child. The solution @wonderlives posted in the dicussion area is really genious. The O(n) solution will use dfs and save the currentpath to a cache. The cache will indicate, e.g. cache[4]:2, there are 2 paths from root to the current node, that has a sum of 4. If the sum of the path from root to the current node is 10, and the target is 6, there will be two paths from root to some intermediate node summed to 4 and from these two nodes to current node is 6, and summing them up is 10. After reach the leaf node, we need to reduce the cache[currentPathSum] by 1 because leaving leaf node means to back to its parent node, in this case, the currentPathSum which is the sum from root to the leaf node will not longer be valid.

I have to say this is a genious solution, and this problem should be rated as medium instead of easy.

The solution's link is: https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)

## 