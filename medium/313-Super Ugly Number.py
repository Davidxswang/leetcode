"""
https://leetcode.com/problems/super-ugly-number/
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""

# time complexity: O(n*m), space complexity: O(n+m) where n is n and m is the length of primes list
# the trick here is to be careful with the primes[j] * result[pointers[j]] <= result[i-1], in this case, we need to move the pointer to the right until it's larger than result[i-1], otherwise this primes[j] will never to used again.

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        result = [0] * n
        result[0] = 1
        pointers = [0] * len(primes)
        for i in range(1, n):
            temp = 2**31
            pointer = None
            for j in range(len(primes)):
                while primes[j] * result[pointers[j]] <= result[i-1]:
                    pointers[j] += 1
                if primes[j] * result[pointers[j]] < temp:
                    temp = primes[j] * result[pointers[j]]
                    pointer = j
            result[i] = temp
            pointers[pointer] += 1
        
        return result[-1]
            
