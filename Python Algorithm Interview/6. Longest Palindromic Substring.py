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
s = 'abcde' 

for i in range(len(s), 0, -1): 
    for j in range(0, len(s) - i + 1):
        if s[j:j+i] == s[j:j+i][::-1]: # s[0:5:1] == s[4:-1:-1]
            print('t',s[j:j+i])
