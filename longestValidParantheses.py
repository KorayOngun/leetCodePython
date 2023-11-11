"""
32. Longest Valid Parentheses
Hard
11.9K
372
Companies
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring
.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

Runtime
Details
49ms
Beats 51.87%of users with Python3
Memory
Details
16.37MB
Beats 90.16%of users with Python3

"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left,rigth,max = 0,0,0
        for p in s:
            if p == "(":
                left = left+1
            elif p == ")":
                rigth = rigth+1

            if left == rigth:
                max = left*2 if (left*2) > max else max
            if rigth > left:
                    left = 0
                    rigth = 0   
        left,rigth = 0,0
        for p in s[::-1]:
            if p == ")":
                rigth = rigth+1
            elif p == "(":
                left = left+1

            if left == rigth:
                max = rigth*2 if (rigth*2) > max else max
            if rigth < left:
                    left = 0
                    rigth = 0  
        return max
