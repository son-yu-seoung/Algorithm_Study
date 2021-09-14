# 49. Group Anagrams
# Q. Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input : strs = ["eat","tea","tan","ate","nat","bat"]
# Output : [["bat"],["nat","tan"],["ate","eat","tea"]] 

# Example 2:
# Input : strs = [""]
# Output : [[""]]
 
# Example 3:
# Input : strs = ["a"]
# Output : [["a"]]

# My solution -> Time Limit Exceeded
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        result = []
        copy = strs[:]
        for i in range(len(strs)):
            group = []
            for e in copy[:]:
                if Counter(strs[i]) == Counter(e):
                    group.append(e)
                    copy.remove(e)
            if group:
                result.append(group)
        return result

# Optimal solution1
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        import collections
        
        # If you try to insert a key that does not exist, a KeyError is raised.
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())



        

