"""
https://leetcode.com/problems/heaters/
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.


Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.


Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""

# This problem is interesting, but not hard.
# time complexity: O(mlogm+nlogm), where m and n is the length of heaters and houses list
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if len(houses) == 0 or len(heaters) == 0:
            return 0

        self.sort(heaters)
        self.radius = 0
        for i in houses:
            self.minRadius(i, heaters)
        return self.radius

    def sort(self, heaters: List[int]) -> None:
        if len(heaters) == 1:
            return
        self.dividesort(heaters, 0, len(heaters) - 1)

    def dividesort(self, heaters: List[int], start: int, end: int) -> None:
        if start >= end:
            return
        import random
        pivot = random.randrange(start, end + 1)
        heaters[start], heaters[pivot] = heaters[pivot], heaters[start]
        i = j = start + 1
        while j <= end:
            if heaters[j] < heaters[start]:
                heaters[i], heaters[j] = heaters[j], heaters[i]
                i += 1
            j += 1
        heaters[i - 1], heaters[start] = heaters[start], heaters[i - 1]
        self.dividesort(heaters, start, i - 2)
        self.dividesort(heaters, i, end)

    def minRadius(self, housepos: int, heaters: List[int]) -> None:
        i, j = 0, len(heaters) - 1
        if heaters[i] >= housepos:
            mindis = heaters[i] - housepos
            self.radius = mindis if mindis > self.radius else self.radius
        elif heaters[j] <= housepos:
            mindis = housepos - heaters[j]
            self.radius = mindis if mindis > self.radius else self.radius
        else:
            while True:
                middle = i + (j - i) // 2
                if heaters[middle] == housepos:
                    return
                elif j - i == 1 and heaters[i] < housepos < heaters[j]:
                    mindis = min(heaters[j] - housepos, housepos - heaters[i])
                    self.radius = mindis if mindis > self.radius else self.radius
                    return
                elif heaters[middle] > housepos:
                    j = middle
                else:
                    i = middle
