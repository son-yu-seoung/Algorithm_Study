# 344. Reverse String
# Q. Write a function that reverse a string. The input string is given as an array of characters s.

# Example 1:
# Input : s = ["h", "e", "l", "l", "o"]
# Output : ["o", "l", "l", "e", "h"] 

# Example 2:
# Input : s = ["H", "a", "n", "n", "a", "h"]
# Output : ["h", "a", "n", "n", "a", "H"]

# My solution
def reverseString(self, s: List[str]) -> None:
    s[::1] = s[::-1]

# Other solution 1
def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s)-1
    s[left], s[right] = s[right], s[left]
    left += 1
    right += 1

# Other solution 2
def reverseString(self, s: List[str]) -> None:
    s.reverse()
