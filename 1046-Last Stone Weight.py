"""
https://leetcode.com/problems/last-stone-weight/
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""



# time complexity: O(nlogn), space complexity: O(1)
# author @lee215 claimed this time complexity is O(n^2), but I think it's O(nlogn), the time complexity of insort is O(logn), same with heap

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # import bisect
        # stones.sort()
        # while len(stones) > 1:
        #    stone1 = stones.pop()
        #    stone2 = stones.pop()
        #    if stone1 > stone2:
        #        bisect.insort(stones, stone1-stone2)
        # return stones[0] if len(stones)==1 else 0

        # this is provided by the solution from @lee215
        A = stones
        A.sort()
        while len(A) > 1:
            bisect.insort(A, A.pop() - A.pop())
        return A[0]


# time complexity: O(nlogn), space complexity: O(1)
# this is provided by the solution from @lee215


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        # h = [-x for x in stones]
        # heapq.heapify(h)
        # while len(h) > 1:
        #    heapq.heappush(h, heapq.heappop(h)-heapq.heappop(h))
        # return -h[0]