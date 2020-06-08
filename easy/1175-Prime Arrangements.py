"""
https://leetcode.com/problems/prime-arrangements/
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015


Constraints:

1 <= n <= 100
"""

# time complexity: O(n^(1.5)) due to the prime number searching process if using commented way, O(n) if using seive
# space complexity: O(1) if using counting, O(n) if using seive.

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        """
        primenumber = 0
        for i in range(2, n+1):
            if self.isPrime(i):
                primenumber += 1
        """
        l = [True] * (n + 1)
        l[0] = l[1] = False
        for i in range(2, len(l)):
            if l[i]:
                for j in range(2 * i, len(l), i):
                    l[j] = False
        primenumber = sum(l)
        return self.fac(primenumber) * self.fac(n - primenumber) % (10 ** 9 + 7)

    import functools
    @functools.lru_cache()
    def fac(self, number: int) -> int:
        if number <= 1:
            return 1
        return number * self.fac(number - 1)

    def isPrime(self, number: int) -> bool:
        if number == 1:
            return False
        if number == 2:
            return True
        import math
        for i in range(2, int(math.sqrt(number)) + 2):
            if number % i == 0:
                return False
        return True