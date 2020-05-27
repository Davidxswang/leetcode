"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""

# I didn't come up with these solutions. Thanks to @lccn345 in the discussion area.

# time complexity: O(nlogn), space complexity: O(k), where n is the length of nums
# the time is really spent on the heap popping process in the init
# This is a very classic problem solved by heap.

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


# This uses bisect.bisect_left to help find the insert position and list slice to update the list, very genious.
# time complexity: O(nlogn), space complexity: O(k)
# the time is really spent on the sorting process of nums

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        import bisect
        i = bisect.bisect_left(self.nums, val)
        if len(self.nums) < self.k:
            self.nums[:i] = self.nums[:i]+[val]
        elif i:
            self.nums[:i] = self.nums[1:i]+[val]
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)



# time complexity: O(nlogn), space complexity: O(k)
# it's very interesting here that we didn't remove any item from self.nums after adding.
# There are several reason I guess:
# 1. the time complexity is dominated by sorting not by adding. sorting is nlogn, but inserting is n.
# 2. the add operation is not too frequent, so that the length of the list is not too long.

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        import bisect
        bisect.insort(self.nums, val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)