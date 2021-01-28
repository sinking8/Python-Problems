'''
Difference between LCM and HCD of two numbers.
Two whole numbers N1 and N2 are passed as input. The program must print the difference between LCM and HCF of these two numbers.

INPUT:
First line contains N1 and N2 separated by a space

OUTPUT:
The first line should contain the difference between LCM and HCF of N1 and N2

CONSTRAINTS:
1<= N1, N2 <= 10^3

SAMPLE INPUT:
30 45

SAMPLE OUTPUT: 
75

EXPLANATION: 
LCM is 90, HCF is 15. Difference = 90-15 = 75

SAMPLE INPUT 1:
100 120

SAMPLE OUTPUT1:
580

SAMPLE INPUT 2:
3 4

SAMPLE OUTPUT 2:
11

SAMPLE INPUT 3:
10 20

SAMPLE OUTPUT 3:
15

SAMPLE INPUT 4:
20 30

SAMPLE OUTPUT 4:
50

SAMPLE INPUT 5:
50 120

SAMPLE OUTPUT 5:
590

'''

N1, N2 = map(int,input().split())
lcm, hcf = 0, 0
for i in range(1,min(N1,N2)):
	if(N1%i == 0 and N2%i == 0): hcf = i;

great = max(N1,N2)
while(True):
	if((great%N1 == 0) and (great%N2 == 0)):
		lcm = great
		break
	great+=1
print(lcm-hcf)
