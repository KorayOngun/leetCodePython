"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
Accepted
2.3M
Submissions
7M
Acceptance Rate
32.4%
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        c = len(s)
        for i in range(c-1,-1,-1):
            for j in range(0,c-i):
                t = s[0+j:i+1+j]
                _t = t[::-1]
                if t == _t:
                    if _t in s:
                        return t
                    
