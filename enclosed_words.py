'''
Enclose Words
Given N words separated by a space enclose the word M by double quotes.

INPUT:
First line contains N
Second line contains N words separated by a space
Third line contains M word

OUTPUT:
Display the altered words separated by a space

CONSTRAINTS:
1<= N <= 10*3

SAMPLE INPUT:
6
fox lion tiger doll cat lion
lion

SAMPLE OUTPUT: 
fox “lion” tiger doll cat “lion”

EXPLANATION: 
All occurences of lion in S are enclosed within double quotes
Hence the altered words would be fox “lion” tiger doll cat “lion”

SAMPLE INPUT 1:
2
cat dog
king

SAMPLE OUTPUT 1:
cat dog

SAMPLE INPUT 2:
3
apple orange banana
apple

SAMPLE OUTPUT 2:
"apple" orange banana

SAMPLE INPUT 3:
4
a b c d
d

SAMPLE OUTPUT 3:
a b c "d"

SAMPLE INPUT 4:
4
a a a a
a

SAMPLE OUTPUT 4:
"a" "a" "a" "a"

SAMPLE INPUT 5:
5
run run go away
run

SAMPLE OUTPUT 5:
"run" "run" go away
s
'''
N  = int(input());wrds = list(map(str,input().split()));
M = input().strip()
for word in wrds:
	if(word == M):print('"%s"'%(word),end=" ")
	else:print(word,end=" ")