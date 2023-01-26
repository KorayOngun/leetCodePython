"""""
You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
Accepted
150.7K
Submissions
467.2K
Acceptance Rate
32.2%
"""""

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == "" : return s
        if s == s[::-1] : return s
        c1 = len(s)-1
        c2 = c1-1
        while s[c1:c2:-1]+s != (s[c1:c2:-1]+s)[::-1]:
            c2 = c2-1
        return s[c1:c2:-1]+s 
        
res = Solution().shortestPalindrome("abcd")
print(res)
