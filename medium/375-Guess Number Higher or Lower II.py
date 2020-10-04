"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/

We are playing the Guessing Game. The game will work as follows:

I pick a number between 1 and n.
You guess a number.
If you guess the right number, you win the game.
If you guess the wrong number, then I will tell you whether the number I picked is higher or lower, and you will continue guessing.
Every time you guess a wrong number x, you will pay x dollars. If you run out of money, you lose the game.
Given a particular n, return the minimum amount of money you need to guarantee a win regardless of what number I pick.

 

Example 1:


Input: n = 10
Output: 16
Explanation: The winning strategy is as follows:
- The range is [1,10]. Guess 7.
    - If this is my number, your total is $0. Otherwise, you pay $7.
    - If my number is higher, the range is [8,10]. Guess 9.
        - If this is my number, your total is $7. Otherwise, you pay $9.
        - If my number is higher, it must be 10. Guess 10. Your total is $7 + $9 = $16.
        - If my number is lower, it must be 8. Guess 8. Your total is $7 + $9 = $16.
    - If my number is lower, the range is [1,6]. Guess 3.
        - If this is my number, your total is $7. Otherwise, you pay $3.
        - If my number is higher, the range is [4,6]. Guess 5.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $5.
            - If my number is higher, it must be 6. Guess 6. Your total is $7 + $3 + $5 = $15.
            - If my number is lower, it must be 4. Guess 4. Your total is $7 + $3 + $5 = $15.
        - If my number is lower, the range is [1,2]. Guess 1.
            - If this is my number, your total is $7 + $3 = $10. Otherwise, you pay $1.
            - If my number is higher, it must be 2. Guess 2. Your total is $7 + $3 + $1 = $11.
The worst case in all these scenarios is that you pay $16. Hence, you only need $16 to guarantee a win.
Example 2:

Input: n = 1
Output: 0
Explanation: There is only one possible number, so you can guess 1 and not have to pay anything.
Example 3:

Input: n = 2
Output: 1
Explanation: There are two possible numbers, 1 and 2.
- Guess 1.
    - If this is my number, your total is $0. Otherwise, you pay $1.
    - If my number is higher, it must be 2. Guess 2. Your total is $1.
The worst case is that you pay $1.
 

Constraints:

1 <= n <= 200
"""

# time complexity: O(n^3), space complexity: O(n^2)
# the solution is insipred by @10000tb: https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84762/Improve-the-Question-and-Example/89343
# so the best solution for cost(start=1, end=n) is min(k + max(cost(start=1, end=k-1), cost(start=k+1, end=n)))
# which means we need to pay for the guess of k, then add to it the cost of left part (when we get the signal smaller) or the cost of right part (when we get the signal larger), whichever is larger, because we need to make sure no matter what number they think of, we can win, using the money

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        table = [[float('inf')] * (n+1) for _ in range(n+1)]
        for k in range(0, n):
            for start in range(1, n-k+1):
                end = start + k
                if k == 0:
                    table[start][end] = 0
                elif k == 1:
                    table[start][end] = start
                elif k == 2:
                    table[start][end] = start + 1
                else:
                    table[start][end] = min(
                        mid+max(table[start][mid-1], table[mid+1][end]) for mid in range(start+1, end)
                    )
        return table[1][n]