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

strs = ["mod","mop","pip","tug","hop","dog","met","zoe","axe","mug","fdr","for","fro","fdr","pap","ray","lop","nth","old","eva","ell","mci","wee","ind","but","all","her","lew","ken","awl","law","rim","zit","did","yam","not","ref","lao","gab","sax","cup","new","job","new","del","gap","win","pot","lam","mgm","yup","hon","khz","sop","has","era","ark"]
from collections import Counter
group = []

for i in range(len(strs)):
    temp = [strs[i]]

    for j in range(i+1, len(strs)):
        if Counter(strs[i]) == Counter(strs[j]): # anagrams find
            temp.append(strs[j])
    
    group.append(temp)

group.sort(key=lambda x: len(x), reverse=True)
temp_idx = set()

for i in range(len(group)): # overlap index collect
    for j in range(i+1, len(group)):
        for z in range(len(group[j])):
            if group[j][z] in group[i]:
                temp_idx.add(j)

temp_idx = list(temp_idx) # set -> list & sort() for correct delete
temp_idx.sort()

for i, value in enumerate(temp_idx):
    del group[value-i]

return group
