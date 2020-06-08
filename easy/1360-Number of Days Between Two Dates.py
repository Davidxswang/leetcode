"""
https://leetcode.com/problems/number-of-days-between-two-dates/
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

# time complexity: O(n), space complexity: O(1)

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 == date2:
            return 0
        date1, date2 = (date1, date2) if date1 < date2 else (date2, date1)
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year1, month1, day1 = int(date1[0:4]), int(date1[5:7]), int(date1[8:])
        year2, month2, day2 = int(date2[0:4]), int(date2[5:7]), int(date2[8:])
        past1 = 0
        for y in range(1971, year1):
            past1 += 366 if self.is366(y) else 365
        months[2] = 29 if self.is366(year1) else 28
        for m in range(month1):
            past1 += months[m]
        past1 += day1
        
        past2 = 0
        months[2] = 29 if self.is366(year2) else 28
        for y in range(1971, year2):
            past2 += 366 if self.is366(y) else 365
        for m in range(month2):
            past2 += months[m]
        past2 += day2
        return past2 - past1
    
    
    def is366(self, year: int) -> bool:
        return year % 100 == 0 and year % 400 == 0 or year % 100 != 0 and year % 4 == 0

