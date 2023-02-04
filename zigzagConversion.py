""" 
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
Accepted
973K
Submissions
2.2M
Acceptance Rate
44.6%
"""



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        elif len(s)>numRows:
            list1 = [ "" for x in range(numRows)]
            c = 0
            down = True
            for i in range(len(s)):
                if down == True:
                    list1[c] = list1[c] + s [i]
                    c = c + 1 
                    if c == numRows:
                        c = c - 2 
                        down = False
                else:
                    list1[c] = list1[c] + s[i]
                    c = c - 1
                    if c == -1:
                        c = c + 2 
                        down = True
            a = ""
            for i in list1:
                a = a+i
            return a
        else:
            return s
        

"""


Koray öngün
Feb 04, 2023 18:12

Python3

Runtime
59 ms
Beats
76.35%


Memory
14 MB
Beats
48.51%
"""