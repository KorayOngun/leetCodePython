""""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
Accepted
1.9M
Submissions
3.6M
Acceptance Rate
54.2%
"""

values = [1,10,6,2,5,4,10,3,7]
c1 = 0
c2 = len(values)-1
m = 0
while c1<c2:
    a = min(values[c1],values[c2])*(c2-c1)
    m = max(m,a)
    print(m)
    if values[c1] <= values[c2]:
        c1 = c1+1
    else:
        c2 = c2-1
