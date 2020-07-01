"""

https://leetcode.com/problems/bitwise-and-of-numbers-range/
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""

# time complexity: O(logn), space complexity: O(1)
# the genious solution is provided by @GatsbyLee in the discussion area.

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        This is the most simplest solution that I have ever seen, but it's not easy to prove its correctness.
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
        
        Proved (badly though).#.
        """
        x = n
        while x > m:
            x &= x-1
        return x
        
    
        """
        A common way of doing this is to find the common prefix of m and n directly
        """
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return m << i
