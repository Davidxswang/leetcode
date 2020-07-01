# What Is This?
I decided to go through the LeetCode problems 10/day, and publish some of the solutions here. Hopefully it will be helpful for myself or some of you that are in front of the screen.

Notes: space complexity by defaulted is counted by the extra space used by the program, omitting the call stack and the output variables.

Now solutions to all the public easy problems have been posted here. Those easy problems that are not public are not included in this repository.

# Some Interesting Problems
## Easy Problems
### 28 Implement strStr()
KMP pattern search algorithm use a O(m+n) time complexity to search a substring in a string, which is really incredible. The key actually is to make use of the information embedded in the pattern string.

### 53 Maximum Subarray()
#### Divide and Conquer
Every time, it divides the array into two parts, calculates the maximum subarray in each part(left and right), and the array that is across the middle element. Max(left sum, right sum, the sum across the middle element) is the result of that level.
#### Dynamic Programming
Kadane's algorithm uses the assumption that whenever I evaluate a new element nums[i] and check if I should connect it to a already-found subarray previously to make a contiguous subarray, the previous part should not lower the current value nums[i]. Otherwise I should start from nums[i] + 0 instead of nums[i] + Negative Value.

### 371 Sum of Two Integers
When solving this problem, I found the post that @LHearen wrote was very useful, so I suggest that every one who is working on LeetCode take a look at [this post](https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently).

### 437 Path Sum III
Given a binary tree, find the number of paths that sum to a given value. The path can start and end anywhere as long as start -> end is parent -> child. The solution @wonderlives posted in the dicussion area is really genious. The O(n) solution will use dfs and save the currentpath to a cache. The cache will indicate, e.g. cache[4]:2, there are 2 paths from root to the current node, that has a sum of 4. If the sum of the path from root to the current node is 10, and the target is 6, there will be two paths from root to some intermediate node summed to 4 and from these two nodes to current node is 6, and summing them up is 10. After reach the leaf node, we need to reduce the cache[currentPathSum] by 1 because leaving leaf node means to back to its parent node, in this case, the currentPathSum which is the sum from root to the leaf node will not longer be valid.

I have to say this is a genious solution, and this problem should be rated as medium instead of easy.

Check out the [solution](https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A).

### 121 Best Time to Buy and Sell Stock
Actually this is a dynamic programming problem. We can only sell and buy at most once on the market. This is very similar to the **53 Maximum Subarray** question.

- If the current CHANGE makes me earn money(current balance > 0), I should embrace the change. -> compare this with maxprofit.

- If the current CHANGE makes me lose money(current balance < 0), I should start over. -> reset the current balance = 0.

### 160 Intersection of Tow Linked Lists
I found the genious solution from the discussion area, by @icrtiou. [Check it out.](https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments)

Basically this is make two lists connected, one is A+B, the other is B+A. These two will have the same length. Use two pointers to go from the beginning of each connected list and see if these two pointers will be the same.

There are two cases that these two pointers will be the same:
- when they are both None, which will be at the end. This means they don't share any common element.
- when they have some common element and they are both pointing to that element at the same time.

This is a very brilliant idea.

### 189 Rotate Array.
Thanks to @danny6514 in the discussion area. [Check it out.](https://leetcode.com/problems/rotate-array/discuss/54250/Easy-to-read-Java-solution) This is genious, but very easy to interpret.

To rotate, is to put the last few digits in the front. This can be thought as: 
    
    1. Reverse the whole list first so that the few digits are in the front, but all the digits are in the wrong order.
    
    2. Then, reverse the first few digits that are supposed to move from the back to the front.
    
    3. At last, reverse the last few digits that are supposed to move from the front to the back.

### 204 Count Primes
I didn't think out the solution. Thanks to @tusizi in the discussion area. [Solution link.](https://leetcode.com/problems/count-primes/discuss/57595/Fast-Python-Solution)

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

### 172 Factorial Trailing Zeroes
Thanks to @xcv58 in the discussion area. [Check it out.](https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages)

The trailing zeros depend on the number of 5 in n! because there are way more 2s than 5s in n!.

To calculate the number of 5 in n!, we need to calculate there are how many numbers in n! containing:
    
    5, like: 5, 10, 15, 20, 25, 30, 35...
    25, like 25, 50
    125, like 125, 250
    ...

    Take a close look, we can see if the number is like 5, 10, 15, 20, 55, 65, even though they are greater than 5, they only contain one 5
    
    But for numbers like 25, 50, they contain two 5s, i.e. they have 25 in them.
    
    Therefore, we need to calculate iteratively.

### 198 House Robber
It's a dynamic programming problem. The core idea is that the current maximum profit is whether:

- from robbing current house + the maximum profit in house current-2 house, or,

- from not robbing current house, i.e. the maximum profit in the current house == the maximum profit in the current-1 house,

whichever is larger should be the maximum profit in the current house.

This is inspired by @heroes3001 in the discussion area. [Check it out.](https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.)

### 234 Palindrome Linked List
This is inspired by @yavinci in the discussion area. [Check it out.](https://leetcode.com/problems/palindrome-linked-list/discuss/64501/Java-easy-to-understand)

Use slow and fast pointer to find the middle+1 element. If 6, it's 4, if 5, it's 4.

Then reverse the second half, e.g. if 6, reverse 4-6, if 5, reverse 4-5.

Compare the element one by one on the first and second half.

It's not hard at all, just need to be careful with all the details.

### 543 Diameter of Binary Tree
Thanks for the solution provided by the problem. 

The main idea is to traverse all the node, and see if left+right+1 is larger than current max. If it's larger, update the global variable. After finish dfs of this node or this subtree, return max(left,right)+1.

[Here is the solution.](https://leetcode.com/problems/diameter-of-binary-tree/solution/)

### 572 Subtree of Another Tree
The key idea is to traverse very node in the tree, and treat each node as a root of tree A to see if tree A is equal to t. Thanks to the [solution.](https://leetcode.com/problems/subtree-of-another-tree/solution/)

Time complexity: O(nm) where n and m are the numbers of elements in tree s and t.

Space complexity: O(depth of s) if recursion is considered.

### 581 Shortest Unsorted Continuous Subarray
Three traverses to find the answer. Thanks to the solution provided in the solution.

    - The first traverse is to find the the beginning and end of a reverse pair. A reverse pair is two nums such that nums[i] > nums[i+1].

    - The second traverse is to find the min and max of the nums in nums[start] to nums[end]

    - The third traverse is to find where the locations that min and max should be put if we were going to sort the array. Note in the 3rd traverse that we should find the element that nums[i] > min for start and nums[i] < max for end. Equality is excluded in both situations because first is the violation of the <= rule and second is to find the shortest subarray.

Time complexity: O(n), space complexity: O(1)

### 605 Can Place Flowers
Dynamic programming problem. Greedily search the available spot and put the plant there see how many we can place in the list.

Thanks to the solution provided by @awice and @PhilF in the discussion area. [Link is here.](https://leetcode.com/problems/can-place-flowers/discuss/103890/Python-Straightforward-with-Explanation)

### Maximum Product of Three Numbers
This is not a hard question, just need to think thoroughly. Given a sequence, the maximum product of three numbers happens either in following three cases:
    
    1. maximum < 0. In this case, we should find the maximal 3 numbers to make the product maximum.
    
    2. maximum = 0. In this case, we can find 0 and another 2 negative numbers to make the product = 0, which is largest.
    
    3. maximum > 0. In this case, we can find the maximum by max[0]*max[1]*max[2] or max*min[0]*min[1] whichever is larger.
    
So combining them all together, we can get: max = max(max[0]*max[1]*max[2], max*min[0]*min[1]).

Thanks to the solution provided by the questions. [Check it out.](https://leetcode.com/problems/maximum-product-of-three-numbers/solution/)

### 653 Two Sum IV
To save the extra space (space due to call stack omitted), I used two iterators to traverse the tree, one from left to right, the other from right to left, therefore two pointers are going toward each other.

- If two pointers (from two iterators) meet but still could not find a match, search fails. 

- If two pointers have not meet but have the same node values not summed up to k, search fails, because when traversing inorderly, the same elements are contiguous.

- If two pointers summed up are too small, move the left pointer toward right a step further. 

- If two pointers summed up are too large, move the right pointer toward left a step further.

Hope you find this solution interesting. I also posted this solution here, [check it out.](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/discuss/647955/Python-Solution-Time-O(n)-Space-O(1)-using-Iterator-Yield)

### Second Minimum Node In a Binary Tree
Thanks for the solution provided by the problem. The basic idea is

- The global minimum is root.val for sure.

- If we find another one larger than minimum, it's the potential answer.

- If we find a node that is equal to or larger than the potential answer, than we don't need to check the left and right substree of this node, because this node is the smallest of that subtree.

- If we find a node that is smaller than the potential answer (surely larger than the global min), we need to replace the potential answer by this number and we don't need to check its left and right subtrees. Reason same as above.

- If we find a node that is equal to the global minimum, we need to traverse its left and right subtrees because we might find better potential answer in the subtrees.

Time complexity: O(n), space complexity: O(1)

### 680 Valid Panlindrome
Thanks for the solution provided by the problem. The idea behind is very easy:

Check from left and right toward the center, if there is a mismatch between s[i] and s[j] (for i < j), there has to be a palindrome either in s[i+1]-s[j] or in s[i]-s[j-1]

Time complexity: O(n), space complexity: O(1)

### 703 Kth Largest Element in a Stream
The solution proposed by @lccn345 in the discussion area is very good. Heap and bisect are used.

[Check it out here.](https://leetcode.com/problems/kth-largest-element-in-a-stream/discuss/639723/AC-simply-readable-Python)

### 696 Count Binary Substrings
I didn't come up with the second solution. Thanks to the solution provided by the question.

It's very trick here because when we finish the traverse, the last pair doesn't get updated to the answer. Therefore, we need to update it by ourselves.

### 836 Rectangle Overlap
The two solutions provided by the problem are both very interesting, worth taking a look. [Here is the link.](https://leetcode.com/problems/rectangle-overlap/solution/)

### 844 Backspace String Compare
The second solution provided by the problem set uses generator and very neat and clean. [Check it out.](https://leetcode.com/problems/backspace-string-compare/solution/)

### 942 DI String Match
The problem seems hard but when you see the solution, you will be surprised by how easily it can be solved.

It always makes the best-for-now and best-for-next decision.

If right now, it's an increase, it's better we put the current smallest available number here; on the other hand, if right now, it's a decrease, it's better we put the current largest available number here.

By this rule, we can use up all the 0..N numbers, and we can guarantee that if there is an increase, the next number is larger than current number and if there is a decrease, the next is smaller than current one.

Very smart solution, and easy to implement. Just hard to think.

### 1029 Two City Scheduling
[@logan138](https://leetcode.com/problems/two-city-scheduling/discuss/667786/Java-or-C%2B%2B-or-Python3-or-With-detailed-explanation) provided a very good solution.

The idea is to send every one to city A. Then we need to send half of them to city B. When we do this, we need to see who can give us the most refund if we send them. So we sort them by refund and send the most refund N people to city B and the rest stay in A.

### 1042 Flower Planting With No Adjacent
This is a very good problem. The solution provided by [@lee215](https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290858/JavaC%2B%2BPython-Greedily-Paint) is very good.

We just need to remember what nodes each node cannot share color with, then we can assign each node a color from those colors that are current available.

### 1089 Duplicate Zeros
In this problem, the edge case is very tricky to deal with. I do two traverses, first to discover the last element to deal with, and second traverse to put every element to the correct place.

In the first traverse, read and write can end up with read == write or ready == write + 1 two are different situations:

- read==write means:
    - read += 1, then read meet write, in this case write did not move at the last move of read
    - read(0), 1, write, after this situation, read += 1 and write -= 1, so read and write meet. 
    - In both cases, this element that write is pointing to at the last, should not be repeated, because this one is literally the last element in the new list.

- read==write+1 means read finds a 0 this is second to the last element of the new list and this 0 should be repeated in this case.

So in the second traversal, we need to deal with these two ending situations to make sure the last element can be taken good care of.

### Remove Palindromic Subsequences
This is a very tricky questions. I got the help from [@lee215](https://leetcode.com/problems/remove-palindromic-subsequences/discuss/490303/JavaC%2B%2BPython-Maximum-2-Operations) in the discussion area.

A very important thing we need to know is that a subsequence of a string doesn't need to be consecutive.

## Medium Problems
### 11 Container With Most Water
This is an interestring question. The volume of the water depends three things:

- the left bar
- the right bar
- distance between left and right bars

For any given pair of bars, the volume depends on the shorter bar. So what we should do is check the volume of current configuration and make the two bar closer by moving the pointer which is pointing the shorter bar closer to the other pointer.

The reason why we do this is that the current configuration is limited by the shorter bar, and by moving it, we might get a change to make the result better. Imagine that we move the longer one and get a even longer bar, but the volume is still limited by the shorter one that we didn't move, which is not what we would want.

### 15 3Sum
This is a very classic question. Thanks to the excellent explanation from [@christopherwu052](https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)). The idea is to first sort the numbers, then for each number, fix it and look all the numbers after it using two pointers. The process of using two pointers to look for a value is just like 2sum.

To make it faster, we can early stop when the fixed number is larger than 0 because there is no way we can make the sum equal to 0 if the smallest of the three is larger than 0.

### 16 3Sum Closest
This is very similar to the question above. The idea is to fix one number and go over the number behind it and the array should be sorted. 

### 17 Letter Combinations of a Phone Number
This is a very good example of recursion. I got the inspiration from the solution provided with the questions.

Every time we can just take a number in the front of the digits and loop in its possible representations and recursively call the recursion process until there is no more digit to extract.

### 22 Generate Parentheses
This is inspired by [@brobins9](https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution) in the discussion area.

The idea behind is to always put '(' in the string first, and then put the same number of ')' in the string. If the length of the string is not enough compared with 2*n, repeat the process above. This is very brilliant.

### 29 Divide Two Integers
This is inspired by [@tusizi](https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code) in the discussion area.

The idea is to subtract a divisor*(2^i) from dividend and if we succeed, we add this 2^i to the result. We repeat the process until dividend < divisor.

### 50 Pow(x, n)
This is very similar to question 29. Every time multiply a x^(2^i) to the result and subtract 2^i from n, until n == 0.
 

### 31 Next Permutation

This is inspired by [@yuyibestman](https://leetcode.com/problems/next-permutation/discuss/13866/Share-my-O(n)-time-solution) in the discussion area. 

In the Wikipedia, it says this method actually came from Narayana Pandita in 14th century India. The method is:
	1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
	2. Find the largest index l greater than k such that a[k] < a[l].
	3. Swap the value of a[k] with that of a[l].
	4. Reverse the sequence from a[k + 1] up to and including the final element a[n].

### 34 Find First and Last Position of Element in Sorted Array
It is inspired by [@baby_groot](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14699/Clean-iterative-solution-with-two-binary-searches-(with-explanation)) in the discussion area.

His (I assume it's he) code is very concise and elegant. The idea is to not stop and return when finding one target, instead, we should let the program narrow down until left and right points to the same element. In this case, either we have found the element, or there is no such target. If we have found such target, we can find leftmost one and the rightmost one.

The trick here is how to deal with the *equal* case.

### 43 Multiply Strings
This is inspired by [@yavinci](https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation) in the discussion area.

The idea is to multiply each digit of num1 by each digit of num2 and put them in the right place in the result string. Then sum all the numbers in the same spot in the result string.

I have to say this is a very elegant way of solving this problem.

### 55 Jump Game
This is a very classic dynamic programming problem.

	1. If from position A, one can jump to the last element, position A is good.
	2. The last element is good.
	3. If the leftmost good element is within the jump range of the current element, the current element is good as well.
	4. Now what we need to do is just check whether position=0 is good or not.

### 77 Combinations
[@vision57](https://leetcode.com/problems/combinations/discuss/27024/1-liner-3-liner-4-liner) in discussion area provided a very good post.

There are basically two ways to solve this question: iteration or recursion. Recursion is fast, but consumes a lot of space. 

### 75 Sort Colors
[@girikuncoro](https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation) pointed out that this is a Dutch partition problem, [wiki](https://en.wikipedia.org/wiki/Dutch_national_flag_problem).

The partition is like this: red: [0:red], unclassified(white): [red: blue+1], blue: [blue+1:]. At the beginning three pointers are like this:

- red = 0
- white = 0
- blue = len(nums)-1

Then we need to let white pointer move from left to right until it finishes checking the last unclassified element which should be where blue is.

- if white = 0: swap it with red, then red++,white++. Here we can ++ both becausewhen we start, we can make sure red was 1 before swapping, and after swapping, we can make sure white is 1 now, so we can ++ both.

- if white = 1: white ++, move on.

- if white = 2: this should be put out of the unclassified area, so we swap it with blue and move blue to the left by 1.


### 92 Reverse Linked List II
This question requires us to reverse part of the linked list given the start and end index of the linked list.

The keys here are:

- find the m-1 node
- reverse the m to n nodes
- connect m-1 node with n node, connect m node with n+1 node

It's not easy to think of the solution but it's very tricky to handle the edge cases of the coding.

### 89 Gray Code
This question asks us to build a Gray Code of length n.

The solution is inspired by [@yuyibestman](https://leetcode.com/problems/gray-code/discuss/29891/Share-my-solution) and the code is provided by @zkf85 in the discussion area.

The main idea comes from the symmetricity here: 00,01,11,10 -> (000,001,011,010)(110,111,101,100). The first part actually is the original part from n-1, the second part is built by putting a 1 in the front. 


### 114 Flatten Binary Tree to Linked List
This is a very good question: to flatten a binary tree in preorder. The answer is inspired by [@tusizi](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share) in the discussion area.

The main idea is to traverse the tree in postorder and traverse right node first, then left node, finally root. So this is totally the reverse preorder which is what we want.

When we process each node, we traverse its right, left, then itself. After we finish the right and left children, we are going to set the left node=None, and right node to the node we just finished, which is what the result of left tree produced.

After we are done, the tree is one that every node only has its right child.

### 109 Convert Sorted List to Binary Search Tree
The most interesting solution is provided by this question's solution. 

The way we do it is that we pretend we can find the middle element but we don't really find it directly. Instead, we run the program on left half size and find the left node that it returns, build the root node using the current head, then connect the left node to the root's left, move the head to the next linked node, run the same process on the right half and gets the right node, connect to root's right node. 

I think the key here is to move the head to the right by one, because actually, every time, we reach each valid node, we always move the head by one, and that is the way we generate the list by a binary search tree actually.

It's better to check out the [original page of the solution posted by the question](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/solution/)

### 116 Populating Next Right Pointers in Each Node
The solution is inspired by [@yavinci](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37472/A-simple-accepted-solution/35554) in the discussion area.

The main idea is to use the current node/layer to set up its left and right children. It utilizes an implication that root is a single node which can be seen as a completed layer.

### 134 Gas Station
This solution is provided by [@clue](https://leetcode.com/problems/gas-station/discuss/42568/Share-some-of-my-ideas./41006) in the discussion area.

The main idea is to use a gas_needed var to store how much gas at least we should have when we reach the end. If at the end, the gas we have is more than gas_needed, we are okay, and the index that we started is the result, otherwise no solution.

Sure if the total gas is less than total cost, there is no solution, and this should be checked first.


### 137 Single Number
This solution is provided by [@felixhao28](https://leetcode.com/problems/single-number-ii/discuss/43296/An-General-Way-to-Handle-All-this-sort-of-questions./42189) in the discussion area.

The key here is find a way that is commutative and circular, the way we do this is modulo. We can count each bits using a modulo by 3 in this case, then all the effects created by those elements appear 3 times in the array will be eliminated, only the one that appears once is left. Bingo!


### 127 Word Ladder
I think this question should be rated as a hard question. The key here is to build a graph using connectivity which is 1 letter different from each other. Then starting from the beginWord, using Breadth First Search to traverse the graph, if we can meet the endWord, solution is at hand; otherwise, there is no solution. This is so brilliant.

The solutions are provided by the solution set with the question. [Check this out.](https://leetcode.com/problems/word-ladder/solution/)

### 139 Word Break
The solution is inspired by [@segfault](https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways) in the discussion area.

The main idea is to check very position of the array see if it's good. When we say the position i is good, it means s[0:i+1] can be broken using the words in the word array.

- If the s[0:i+1] in word array, i is good.
- If not, look from i to 0 (say it's j), see if j is good and s[j+1:i+1] is in word array, if so, it's good, if not, i is bad.

### 142 Linked List Cycle II
The O(1) space solution is inspired by [@Dico](https://leetcode.com/problems/linked-list-cycle-ii/discuss/44793/O(n)-solution-by-using-two-pointers-without-change-anything/199854) in the discussion area. Also these two videos helped a lot: [linked1](https://www.youtube.com/watch?time_continue=2&v=zbozWoMgKW0) and [link2](https://www.youtube.com/watch?v=LUm2ABqAs1w).

Actually this solution utilizes Floyd's Algorithm to detect the loop:
1. Use slow and fast two pointers to go through the linked list, the speed is 1 and 2 respectively. If they never meet, there is no loop in the linked list.
2. If slow and fast pointers meet at some time, there is a loop, now we need to find the start point of the loop:
3. Let's use q and p pointing to head and the node where slow and fast meet, let them move 1 step forward each time, when they meet, they meet at the start node of the loop.

The videos I mentioned above gave a very good explanation, please check out!

### 148 Sort List
The solution is inspired by [@zdwu](https://leetcode.com/problems/sort-list/discuss/46712/Bottom-to-up(not-recurring)-with-o(1)-space-complextity-and-o(nlgn)-time-complextity) in the discussion area.

This question is very good. The key here is to use a step to control the bucket manually. When we split, we cut two small pieces with length "step" from the list and merge them together; when we merge, we connect them two together and connect it to the formaly finished the tail, and return the tail of the finished list this time.

### 162 Find Peak Element

The main idea here is to use a binary search algorithm to find a peak. Since we only need to find one peak, we can let the search range shrink 1/2 every time. 

The shrink direction is the key. We should let it shrink to the direction where the middle element gets higher.

At the end, when start == end, there is only one element in the search range, this element will be a peak we can return.

Every time when we shrink, we are actually let the middle go uphill, so the edge element in the range will gets higher and higher. This is the reason why it can find a peak.

### 152 Maximum Product Subarray
This solution is inspired by [@mzchen](https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity) in the discussion area. 

Using dynamic programming, we can log the min and max at every position, representing the min and max we can get at every position.

The trick here is when we meet a negative element, we should swap the min and max.

At every position, we should choose to use the prior result (max or min) or not. If we don't use the prior result and we can get better result, then we should not use the prior result. 

### 179 Largest Number
This is provided by the solution set of the question. 

The trick here is to use the subclass to define the less than (<) logic and let the sort method to sort the string using < but it actually gets the string ordered in a descending order.

We can not just use reverse=True argument to reversely sort the string, because that will bring some problem when two strings start with the same prefix, like 30,3 and 3,30 in the example of the question.

The logic of < is: if a+b > b+a, a should go first in the list because this will provide a larger final result.

In the [Python Documentation](https://docs.python.org/3/howto/sorting.html), it says:

> The sort routines are guaranteed to use __lt__() when making comparisons between two objects. So, it is easy to add a standard sort order to a class by defining an __lt__() method.

So we cannot sort the array reversely by overriding __gt__ method.

### 166 Fraction to Recurring Decimal
The solution is inspired by [@tusizi](https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51110/Do-not-use-python-as-cpp-here's-a-short-version-python-code) in the discussion area.

It's not hard to code, it's just not easy to integrate all of these together in such a concise way.

### 201 Bitwise AND of Numbers Range
This is the most simplest solution that I have ever seen, but it's not easy to prove its correctness.
The solution is provided by [@GatsbyLee](https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56729/Bit-operation-solution(JAVA)/58148) in the discussion area.

To prove its correctness, we need to answer these following questions:

1. is the range correct? "while x > m"
	1.1 the start of the range is correct, i.e. we start from n.
	1.2 the end of the range is correct, i.e. the last iteration we should do is when x == m+1, we do x & m, which is correct.
        1.3 what if m == n? the correctness of the algorithm in this case is obvious.

2. is the x &= x-1 correct?
        2.1 suppose every time x & (x-1) give us x-1, then the correctness is obvious.
        2.2 what if x & (x-1) < x-1, say x & (x-1) = x-23? for some x s.t. m < x <= n. Actually x & (x-1) will perserve the common prefix of x and x-1, and set some tail to 0. What we are worried about is the elements that we missed between x-1 and x-23. We don't need to worry because whatever elements between x-1 and x-23, after we do & to all of them, we will get x-23 => the common prefix will always be preserved, the tail 0 will give us 0 always.

3. is the "return x" correct?
        3.1 from 2.2, we can see, x & (x-1) will give us some result. This result is the & of all the elements from [this result, x]. If result > m, we can keep doing this. No problem here.
        3.2 if result == m: return m. The correctness is obvious.
        3.3 if result < m, return result. From 2.2 we know, even though we & the number between x-1 and m, we will still get this "result", so the result is correct.
        
        Proved (badly though)

### 207 Course Schedule
This is inspired by the [solution of problem 210](https://leetcode.com/problems/course-schedule-ii/solution/) and [@hnoss](https://leetcode.com/problems/course-schedule/discuss/58516/Easy-BFS-Topological-sort-Java/59977) in the discussion area.

The main idea is to process each free courses (those don't have prerequisite). After learn the prerequisite courses, its control to the downstream courses can be removed. All the free courses due to this process should be moved to the free courses set until there is no free courses.

If there is no free courses anymore, we need to check if there is remaining edges, if there is any remaining edges, it means all the rest of the courses have a cycle in it because all of them have incoming courses so we cannot start from either of them.

This is very similar to [the 210 question](https://leetcode.com/problems/course-schedule-ii/).
