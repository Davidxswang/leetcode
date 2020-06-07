"""
https://leetcode.com/problems/duplicate-zeros/
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.



Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]


Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""

# this is very tricky about the edge condition. In the first traverse, read and write can end up with read == write or ready == write + 1
# These two are different situations,
# read==write means read += 1 then read meet write, in this case write did not move at the last move of read,
#   or read(0), 1, write, after this situation, read += 1 and write -= 1, so read and write meet.
#   In both cases, this element that write is pointing to at the last, should not be repeated, because this one is literally the last element in the new list.
# read==write+1 means read finds a 0 this is second to the last element of the new list and this 0 should be repeated in this case.
# time complexity: O(n), space complexity: O(1)

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        write = len(arr) - 1    # this points to the last element of the final array
        read = 0                # this points to the element we are scanning
        while read < write:
            read, write = (read+1, write) if arr[read] != 0 else (read+1, write-1)
        lastrepeat = read != write
        read, write = write, len(arr)-1
        while read >= 0 and read <= write:
            if arr[read] != 0 or write == len(arr)-1 and lastrepeat is False:
                arr[write] = arr[read]
                read -= 1
                write -= 1
            else:
                arr[write] = 0
                arr[write-1] = 0
                write -= 2
                read -= 1