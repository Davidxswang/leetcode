"""
https://leetcode.com/problems/merge-intervals/
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

# time complexity: O(nlogn), space complexity: O(1)
# after sorting the array, we can make sure that we only need to compare the beginning of the later interval with the ending of the previous interval
# the time complexity here is very tricky:
#   sorting: O(nlogn)
#   combining: if there is no interval to combine in one pass given starting element, then the pass will only look up 1 element; if all of the intervals need to be combined, then we will delete them all from the list, so there will be only 1 interval left. So the time complexity of this process is actually nearly O(n)
# so the total time complexity is in sorting, O(nlogn)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        i = 0
        while i < len(intervals):
            j = i + 1
            while j < len(intervals):
                if intervals[j][0] > intervals[i][1]:
                    break
                else:
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    intervals.pop(j)
            i += 1
        return intervals
