# 5. Longest Palindromic Substring
# Q. Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input : s = "babad"
# Output : "bab"
# Note : "aba" is also a valid answer.

# Example 2:
# Input : s = "cbbd"
# Output : "bb"

# Example 3:
# Input : s = "a"
# Output : "a"

# Example 4:
# Input : s = "ac"
# Output : "a"

# My solution -> Time Limit Excceded
class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s), 0, -1): 
            for j in range(0, len(s) - i + 1):
                if s[j:j+i] == s[::-1][j:j+i]: # s[0:5:1] == s[4:-1:-1]
                    return s[j:j+i]

# Optimal solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        
        for i in range(len(s)-1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)
        
        return result
        


