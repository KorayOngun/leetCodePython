"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
Accepted
450.1K
Submissions
1.7M
Acceptance Rate
26.9%
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a = "-"+s
        b = "-"+p
        b=b.replace("***","*")
        b = b.replace("**","*")
        
        if p.count("*") == 0 and len(p) != len(s):
            return False
        
        dp = [[False for x in range(len(b))]for i in range(len(a))]
        dp[0][0]=True
        if len(b)>1:
            if   b[1]== "*":
                dp[0][1] = True
        for i in range(1,len(a)):
            for j in range(1,len(b)):
                if a[i] == b[j] or b[j] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif b[j] == "*":
                    dp[i][j]=dp[i-1][j]or dp[i][j-1] or dp[i-1][j-1]
                else:
                    dp[i][j]=False
        
        return dp[-1][-1]