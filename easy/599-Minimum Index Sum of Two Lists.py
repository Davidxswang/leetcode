"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""

# Be careful with the both appear condition, which means we have to make sure the element appears in both lists.
# Or actually we can add 2000 to those element in the index1 that appear in lists2.
# Then when filtering, we set another condition index[key] >= 2000 and index[key] < minimum  or = minimum...
# time complexity: O(n+m), space complexity: O(n+m)
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index1 = dict()
        index2 = dict()
        for i in range(len(list1)):
            index1[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in index1:
                index2[list2[i]] = index1[list2[i]] + i

        minimum = 2000
        result = []
        for key in index2:
            if index2[key] < minimum:
                minimum = index2[key]
                result.clear()
                result.append(key)
            elif index2[key] == minimum:
                result.append(key)
        return result
