"""
https://leetcode.com/problems/day-of-the-week/
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.



Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"


Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

# time complexity: O(y+m+d), space complexity: O(1)

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        past = 0
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for y in range(1971, year):
            past += 366 if self.is366(y) else 365
        months[2] = 29 if self.is366(year) else 28
        for m in range(month):
            past += months[m]
        past += day -1
        past %= 7
        dayname = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        return dayname[past]

    def is366(self, year: int) -> bool:
        if year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
            return True
        return False