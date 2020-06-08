"""
https://leetcode.com/problems/walking-robot-simulation/
A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""

# time complexity: O(m+n), space complexity: O(m), where n and m are the lengths of commands list and obstacles list
# set is really good at handling containing check operation

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        location = (0, 0)
        direction = 0  # north: 0, east: 1, south: 2, west: 3
        maxdistance = 0
        ob = set()
        for obstacle in obstacles:
            ob.add((obstacle[0], obstacle[1]))

        for command in commands:
            if command == -2:
                direction = (direction + 3) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                step = 0
                while step < command:
                    nextLocation = self.getNextLocation(location, direction)
                    if nextLocation in ob:
                        break
                    else:
                        location = nextLocation
                        maxdistance = max(maxdistance, location[0] ** 2 + location[1] ** 2)
                        step += 1

        return maxdistance

    def getNextLocation(self, location: List[int], direction: int) -> (int, int):
        if direction == 0:
            return (location[0], location[1] + 1)
        elif direction == 1:
            return (location[0] + 1, location[1])
        elif direction == 2:
            return (location[0], location[1] - 1)
        elif direction == 3:
            return (location[0] - 1, location[1])
