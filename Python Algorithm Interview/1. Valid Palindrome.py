# 125. Valid Palindrome
# Q. Given a string s, determine if it is a palindrome, 
# considering only alphanumeric characters and ignoring cases.

# Example 1:
# Input: s = "A man a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: s = "race a car"
# Output: false

# My solution
sentence = input()
sentence = sentence.lower()

n = len(sentence)
replace = []

for i in range(n):
    if ord(sentence[i]) >= 97 and ord(sentence[i]) <= 122:

        replace.append(sentence[i])

for i in range(len(replace)//2):
    if replace[i] != replace[-(i+1)]:
        print('false')
        break

    if i+1 == len(replace)//2:
        print('true')

# Optimal solution
import re
def isPalindrom(self, s: str) -> bool:
    s = s.lower()
    # Replace non-lowercase and non-numeric values with ''
    s = re.sub('[^a-z0-9]', '', s) # (regular expression, target string, replacement character)
        
    return s == s[::-1]





    
