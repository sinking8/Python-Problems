'''
Character B follows A
Given a string S and two characters A, B the program must print the number of occurrences where A is followed by B.

INPUT:
First line will contain the string value S.
Second line will contain the value of A.
Third line will contain the value of B. 

OUTPUT:
Display the integer which represents the number of occurrences in string S where A is followed by B.

CONSTRAINTS:
2 <= Length of S <= 200

SAMPLE INPUT:
Malayalam
a
l

SAMPLE OUTPUT: 
2

EXPLANATION: 
There are two occurrences in the string S where a is followed by l is as highlighted below.

SAMPLE INPUT 1:
engine
e
n

SAMPLE OUTPUT 1:
1

SAMPLE INPUT 2:
emblem
e
m

SAMPLE OUTPUT 2:
2

SAMPLE INPUT 3:
anime
a
i

SAMPLE OUTPUT 3:
1

SAMPLE INPUT 4:
glass
a
s

SAMPLE OUTPUT 4:
1

SAMPLE INPUT 5:
inconsistent
i
s

SAMPLE OUTPUT 5:
2

'''
S = input();a = input();b = input();
S_arr = [S[i] for i in range(len(S))];
cnt = 0
while((a in S_arr and b in S_arr) and S_arr.index(a)<S_arr.index(b)):
	S_arr.pop(S_arr.index(a))
	S_arr.pop(S_arr.index(b))
	cnt+=1
print(cnt)