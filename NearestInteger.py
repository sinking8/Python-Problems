'''
Nearest Integer -  Factor
The program must accept an integer N as the input. The program must print the nearest integer of N based on the following conditions.
-	 The concatenation of the first digit and the last digit of the integer must be a factor of the same integer.
-	The nearest integer must be greater than N

INPUT:
Input contains the integer N

OUTPUT:
Display the nearest integer which follows the conditions given

CONSTRAINTS:
1 <= N <= 10^5

SAMPLE INPUT:
103

SAMPLE OUTPUT: 
105

EXPLANATION: 
The nearest possible integer is 105
The concatenation of the first digit and the last digit in 105 is 15
15 is a factor of 105
So 105 is printed as output

SAMPLE INPUT 1:
10

SAMPLE OUTPUT 1:
11

SAMPLE INPUT 2:
123

SAMPLE OUTPUT 2:
130

SAMPLE INPUT 3:
2345

SAMPLE OUTPUT 3:
2349

SAMPLE INPUT 4:
3295923

SAMPLE INPUT 4:
3295929

SAMPLE INPUT 5:
125346

SAMPLE OUTPUT 5:
125350


'''
N = int(input()) + 1
while(True):
	no  = str(N)[0] + str(N)[-1]
	if(N%(int(no)) == 0):
		print(N)
		break
	N+=1