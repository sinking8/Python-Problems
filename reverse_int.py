'''
Reverse Integer
Given an integer N, reverse N and find whether in the reversed N is a factor of N. If it is a factor of N then display yes else display no

INPUT:
Input includes the integer N

OUTPUT:
Display yes it the reversed N is a factor of N else display no

CONSTRAINTS:
1 <= N <= 10^3

SAMPLE INPUT:
20

SAMPLE OUTPUT: 
yes

EXPLANATION: 
N = 20
Reversed N = 2
2 is a factor of 20 hence yes is displayed

SAMPLE INPUT 1:
100

SAMPLE OUTPUT 1:
yes

SAMPLE INPUT 2:
123

SAMPLE OUTPUT 2:
no

SAMPLE INPUT 3:
32425

SAMPLE OUTPUT 3:
no

SAMPLE INPUT 4:
24

SAMPLE OUTPUT 4:
no

SAMPLE INPUT 5:
22

SAMPLE OUTPUT 5:
yes

'''
N = int(input())
reversed_int  = int(str(N)[::-1])
if(N%reversed_int == 0):print("yes")
else:print("no")