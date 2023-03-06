import gzip, sys, re
from collections import Counter

fname = sys.argv[1]
freq_token = {}
list_token = []
list_word = []
freq_word = {}
count_tokens = 0
count_hapex = 0
with open(fname, mode='rt') as infile:
    for line in infile:
        if re.match("\\s+", line):
            continue
        line = line.strip()
        count_tokens += 1
        list_token.append(line.lower())
        list_word.append(line.lower())

freq_token = Counter(list_token)
freq_word = Counter(list_word)
for i in freq_token.keys():
    if freq_token[i] == 1:
        count_hapex += 1
        # list_hapex.append(len(i))
print("Types:", len(freq_token))
print("Tokens:", count_tokens)
print("Haepex:", count_hapex)
# print("Hapex:",sum(list_hapex)/len(list_hapex))

# top 10 tokens
for i in sorted(freq_token, key=lambda x: freq_token[x], reverse=True):
    print(i, freq_token[i])
print()
# most frequent word
for i in sorted(freq_word, key=lambda x: freq_word[x], reverse=True)[:1]:
    print(i, freq_word[i])