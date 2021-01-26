'''
Monkey Jump
A water tank has S steps inside it. A monkey is sitting on the topmost step. The monkey always loves to jump P steps down and Q steps up. In how many jumps will he reach the water level?

INPUT:
The first line contains  S steps inside the water tank
The second line contains P and Q.

OUTPUT:
The first line displays no of jumps require reaching the water level

CONSTRAINTS:
1<= S, P, Q <= 10^3

SAMPLE INPUT:
9
3 2

SAMPLE OUTPUT: 
11

EXPLANATION: 
1st Jump:  1+3 = 4 steps
2nd Jump:  4-2 = 2 steps
3rd Jump:  2+3 = 5 steps
4th Jump:  5-2 = 3 steps
5th Jump:  3+3 = 6 steps
6th Jump:  6-2 = 4 steps
7th Jump:  4+3 = 7 steps
8th Jump:  7-2 = 5 steps
9th Jump:  5+3 = 8 steps
10th Jump: 8-2 = 6 steps
11th Jump: 6+3 = 9 steps
Monkey will reach ninth step in 11 Jumps

SAMPLE INPUT 1:
10
4 2

SAMPLE OUTPUT1:
7
'''
S     = int(input())
P,Q   = map(int,input().split())
strt, jumps, flag = 1, 0, 0 
while(strt<S):
	if(flag%2 == 0):
		strt+=P
	else:
		strt-=Q
	jumps+=1
	flag+=1
print(jumps)