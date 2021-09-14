# 937. Reorder Data in Log Files
# Q. You are given an array of logs. Each log is a space-delimited string of words, 
# where the first word is the identifier.

# There are two types of logs:

# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.

# Reorder these logs so that:

# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

# Example 1
# Input : logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output : ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Example 2
# Input : logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output : ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

# # My solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []

        for i in range(len(logs)): # split lowercase and digits
            str = logs[i].split(' ')[1]
            char = str[0]

            if ord(char) < 58:
                digit_logs.append(logs[i])
            else:
                letter_logs.append(logs[i]) 

        for log_i in range(len(letter_logs)): # buble sort, more study another sort algorithm
            for log_j in range(log_i+1, len(letter_logs)):
                iden1, str1 = letter_logs[log_i].split(' ')[0], letter_logs[log_i].split(' ')[1:]
                iden2, str2 = letter_logs[log_j].split(' ')[0], letter_logs[log_j].split(' ')[1:]

                n_s_1, n_s_2, n_i_1, n_i_2 = len(str1), len(str2), len(iden1), len(iden2)
                n_s, n_i  = min(n_s_1, n_s_2), min(n_i_1, n_i_2)

                for i in range(n_s):
                    if str1[i] > str2[i]:
                        temp = letter_logs[log_i]
                        letter_logs[log_i] = letter_logs[log_j]
                        letter_logs[log_j] = temp
                        break

                    elif str1[i] < str2[i]:
                        break

                    if i == n_s - 1: # all words is same 
                        for i in range(n_i): # identifier sorting
                            try:
                                if iden1[i] > iden2[i] and ord(iden1[i]) > 58:
                                    print(iden1[i], iden2[i])
                                    temp = letter_logs[log_i]
                                    letter_logs[log_i] = letter_logs[log_j]
                                    letter_logs[log_j] = temp
                                    break

                                elif iden1[i] < iden2[i] and ord(iden1) <= 58: # identifier is digit
                                    temp = letter_logs[log_i]
                                    letter_logs[log_i] = letter_logs[log_j]
                                    letter_logs[log_j] = temp
                                    break

                            except: # out of Range
                                if n_i == n_i_2:
                                    temp = letter_logs[log_i]
                                    letter_logs[log_i] = letter_logs[log_j]
                                    letter_logs[log_j] = temp
                        break

        logs = letter_logs + digit_logs
        return logs

# Other solution 1
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    digits, letters = [], []
    for log in logs:
        if log.split()[1].isdigit(): # log.split() defalut is space
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0])) # "let1 art can" -> ("art can", "let1")
    return letters + digits
