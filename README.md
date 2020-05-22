# What is this?
I decided to walk through the LeetCode problems 7/day, and publish some of the solutions here. Hopefully it will be helpful for myself or some of you in front of the screen.

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

The solution's link is: https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A

## 121 Best Time to Buy and Sell Stock
Actually this is a dynamic programming problem. We can only sell and buy at most once on the market. This is very similar to the **53 Maximum Subarray** question.

- If the current CHANGE makes me earn money(current balance > 0), I should embrace the change. -> compare this with maxprofit.

- If the current CHANGE makes me lose money(current balance < 0), I should start over. -> reset the current balance = 0.

## 160 Intersection of Tow Linked Lists
I found the genious solution from the discussion area, by @icrtiou. The link is here: https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments

Basically this is make two lists connected, one is A+B, the other is B+A. These two will have the same length. Use two pointers to go from the beginning of each connected list and see if these two pointers will be the same.

There are two cases that these two pointers will be the same:
- when they are both None, which will be at the end. This means they don't share any common element.
- when they have some common element and they are both pointing to that element at the same time.

This is a very brilliant idea.

## 189 Rotate Array.
Thanks to @danny6514 in the discussion area. https://leetcode.com/problems/rotate-array/discuss/54250/Easy-to-read-Java-solution This is genious, but very easy to interpret.

To rotate, is to put the last few digits in the front. This can be thought as: 
    
    1. Reverse the whole list first so that the few digits are in the front, but all the digits are in the wrong order.
    
    2. Then, reverse the first few digits that are supposed to move from the back to the front.
    
    3. At last, reverse the last few digits that are supposed to move from the front to the back.

## 204 Count Primes
I didn't think out the solution. Thanks to @tusizi in the discussion area. https://leetcode.com/problems/count-primes/discuss/57595/Fast-Python-Solution
The algorithm is the idea of excluding all the numbers that are not prime. I have to say this is very brilliant.

    Step 1, set all the numbers (starting from 2) to prime; 
    
    Step 2, iterate all the numbers, if the number you are inspecting, let's say X, is a prime (by default, it should be a prime unless it has been set not a prime in the previous iteration), set all the numbers that has a factor of X, to "not a prime".

For example, n = 10. 

    If n = 10, the boolean list will be: 
    [False, False, True, True, True, True, True, True, True, True] before the iteration.
    
    After looping on i = 2, the boolean list will be:
    [False, False, True, True, False, True, False, True, False, True].

    After looping on i = 3, the boolean list will be:
    [False, False, True, True, False, True, False, True, False, False].

So the answer for n = 10 is 4.

## 172 Factorial Trailing Zeroes
Thanks to @xcv58 in the discussion area. https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages

The trailing zeros depend on the number of 5 in n! because there are way more 2s than 5s in n!.

To calculate the number of 5 in n!, we need to calculate there are how many numbers in n! containing:
    
    5, like: 5, 10, 15, 20, 25, 30, 35...
    25, like 25, 50
    125, like 125, 250
    ...

    Take a close look, we can see if the number is like 5, 10, 15, 20, 55, 65, even though they are greater than 5, they only contain one 5
    
    But for numbers like 25, 50, they contain two 5s, i.e. they have 25 in them.
    
    Therefore, we need to calculate iteratively.

## 198 House Robber
It's a dynamic programming problem. The core idea is that the current maximum profit is whether:

- from robbing current house + the maximum profit in house current-2 house, or,

- from not robbing current house, i.e. the maximum profit in the current house == the maximum profit in the current-1 house,

whichever is larger should be the maximum profit in the current house.

This is inspired by @heroes3001 in the discussion area. https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.

## 234 Palindrome Linked List
This is inspired by @yavinci in the discussion area. https://leetcode.com/problems/palindrome-linked-list/discuss/64501/Java-easy-to-understand

Use slow and fast pointer to find the middle+1 element. If 6, it's 4, if 5, it's 4.

Then reverse the second half, e.g. if 6, reverse 4-6, if 5, reverse 4-5.

Compare the element one by one on the first and second half.

It's not hard at all, just need to be careful with all the details.

## 543 Diameter of Binary Tree
Thanks for the solution provided by the problem. 

The main idea is to traverse all the node, and see if left+right+1 is larger than current max. If it's larger, update the global variable. After finish dfs of this node or this subtree, return max(left,right)+1.

Here is the solution: https://leetcode.com/problems/diameter-of-binary-tree/solution/

## 