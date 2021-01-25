'''
Concatenation – Common Part

The program must accept a string S and N string values as the input. For each string X among the N string values. 
The program must compare the string S and print the output based on the following conditions.
-	If some characters at end of S are matched with the characters at the beginning of X, the program must concatenate string values S and X so that the common part occurs once.
-	If it’s possible to concatenate the program must print the concatenated string as the input. Else the program must print -1 as the output

INPUT:
The first line contains S
The second line contains N
The next N lines each contains a string value

OUTPUT:
The first N lines each contains the concatenated string or the value -1

CONSTRAINTS:
1<= Length of S and each string value <=100
1<=N<=50

SAMPLE INPUT:
king
2
gsman
worker

SAMPLE OUTPUT:
kingsman
-1

EXPLANATION: 
Here S = ‘king’
The common part between S and 1st string is g. So the concatenated string is kingsman.
There is no common part between S and 2nd String. So -1 is printed.

SAMPLE INPUT 1:
knowledge
7
gender
lodge
ledger
edgeless
edge
dodge
edgeedge

SAMPLE OUTPUT1:
knowledgender
-1
knowledger
knowledgeless
knowledge
-1
knowledgeedge

'''

S = input().strip()
N =  int(input())
for _ in range(N):
	X = input().strip()
	str_pos, flag = 0, False
	for i in range(1,len(X)+1):
		if(X[:i] == S[len(S)-i:]):
			str_pos = i
			flag = True

	if(flag!=True):print('-1')
	else:print(S+X[str_pos:])