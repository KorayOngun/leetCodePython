""""
62. Unique Paths
Medium
13.5K
379
Companies
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
 

Constraints:

1 <= m, n <= 100
Accepted
1.3M
Submissions
2.1M
Acceptance Rate
62.7%



Koray öngün
Apr 10, 2023 23:33

Details
Solution
Python3
Runtime
36 ms
Beats
37.27%
Memory
13.8 MB
Beats
61.62%
"""
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        move_down = m-1
        move_right = n-1
        move_total = move_down + move_right
        return math.comb(move_total,move_right)
