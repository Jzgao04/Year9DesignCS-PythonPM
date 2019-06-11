#Q1
string_1 = input('What is the first string?')
string_2 = input('What is the second string?')

for i in range(len(string_2)):
    if string_1[i] == string_2[i]:
        print(i, string_1[i])

#Q2
'''
from collections import Counter
 
 
def isValid(S):
    char_map = Counter(S)
    char_occurence_map = Counter(char_map.values())
 
    if len(char_occurence_map) == 1:
        return True
 
    if len(char_occurence_map) == 2:
        for v in char_occurence_map.values():
            if v == 1:
                return True
 
    return False
 
 
S = raw_input()
if isValid(S):
    print "YES"
else:
    print "NO"


#Q3
def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = \
                    max(lengths[i+1][j], lengths[i][j+1])
     
    return lengths[-1][-1]
 
def main():
    s1 = raw_input()
    s2 = raw_input()
    print lcs(s1,s2)
     
if __name__ == '__main__':
    main()
'''