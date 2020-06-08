"""
https://leetcode.com/problems/count-primes/
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""

# I didn't think out this solution. Thanks to @tusizi in the discussion area.
# So the algorithm posted is the idea of excluding all the numbers that are not prime. Step 1, set all the numbers (starting from 2) to prime; Step 2, iterate all the numbers, if the number you are inspecting, let's say X, is a prime (by default, it should be a prime unless it has been set not a prime in the previous iteration), set all the numbers that has a factor of X, to "not a prime".
# If n = 10, the boolean list will be:
# [False, False, True, True, True, True, True, True, True, True] before the iteration.
# After looping on i = 2, the boolean list will be:
# [False, False, True, True, False, True, False, True, False, True].
# After looping on i = 3, the boolean list will be:
# [False, False, True, True, False, True, False, True, False, False].
# So the answer for n = 10 is 4.
# time complexity: O(n^1.5), space complexity: O(n)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        isprime = [1] * n
        isprime[0] = isprime[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if isprime[i] == 1:
                for j in range(i * i, n, i):
                    isprime[j] = 0
        return sum(isprime)
