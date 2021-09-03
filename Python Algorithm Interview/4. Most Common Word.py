# 819. Most Common Word
# Q. Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

# Example 1 :
# Input : paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output : "ball"
# Explanation: 
# "hit" occurs 3 times, but it is a banned word.
# "ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is banned.

# Example 2 :

# Input : paragraph = "a.", banned = []
# Output : "a"

# My solution
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # "!?',;." is change ' '
        p_array = [char if 97 <= ord(char) and ord(char) <= 122 else ' ' for char in paragraph.lower()]
        
        p_array = ''.join(p_array) # list element combine to string
        p_array = p_array.split()[:] # split
        
        p_array = [w for w in p_array if w not in banned]

        n_frequent = [p_array.count(i) for i in p_array]
        max_idx = n_frequent.index(max(n_frequent))
        common_word = p_array[max_idx]
        
        return common_word

# Optimal solution
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split() if word not in banned]
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
