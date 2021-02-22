'''
GroupCases
Given a string S which contains both upper case and lower case characters.
Group characters with similar cases.
Display the substring with lower case and the one with upper case.
If the string contains either only upper case or only lower case display -1.

INPUT:
Input a single string S

OUTPUT:
Display the substrings separated by a space if S contains only one case then display -1

CONSTRAINTS:
3<= length of the string S <= 100

SAMPLE INPUT:
SaMkIn

SAMPLE OUTPUT: 
akn  SMI

EXPLANATION: 
In the above string SaMkIn
The lower case characters are a, k, n
The upper case characters are S, M, I
They are grouped and hence akn SMI is printed.

SAMPLE INPUT 1:
ABCdef

SAMPLE OUTPUT 1:
def ABC

SAMPLE INPUT 2:
fginKing

SAMPLE OUTPUT 2:
fgining K

SAMPLE INPUT 3:
ABCDEF

SAMPLE OUTPUT 3:
-1

SAMPLE INPUT 4:
asdigwi

SAMPLE OUTPUT 4:
-1

SAMPLE INPUT 5:
aNtnT

SAMPLE OUTPUT 5:
atn NT

'''
S = input().strip()
S_lst = [S[i] for i in range(len(S))]
S_lower = [i for i in filter(lambda x: x.islower(), S_lst)]
S_upper = [i for i in filter(lambda x: x.isupper(), S_lst)]

if(len(S_lower) != 0 and len(S_upper) !=0):
	print(''.join(s for s in S_lower),''.join(s for s in S_upper))
else:
	print(-1)