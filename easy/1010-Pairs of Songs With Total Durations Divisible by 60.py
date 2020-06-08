"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
In a list of songs, the i-th song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""

# time complexity: O(n), space complexity: O(1) because the upper bound of dic is 61, so it's constant regardless of the size of n

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = dict()
        for i in time:
            remainder = i % 60
            dic[remainder] = dic.get(remainder, 0) + 1

        result = 0
        for i in range(1, 30):
            if i in dic and 60 - i in dic:
                result += dic[i] * dic[60 - i]
        if 0 in dic:
            result += dic[0] * (dic[0] - 1) // 2
        if 30 in dic:
            result += dic[30] * (dic[30] - 1) // 2
        return result