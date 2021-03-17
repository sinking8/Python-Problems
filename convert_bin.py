'''
Convert Binary
Given a number N find the binary equivalent of the number N and replace 1’s for 0’s and 0’s for 1’s. Display the decimal equivalent for the final altered binary number.

INPUT:
Input contains the number N

OUTPUT:
Display the decimal equivalent of the altered binary number.

CONSTRAINTS:
1 <= N <= 10^3

SAMPLE INPUT:
2

SAMPLE OUTPUT: 
1

EXPLANATION: 
The binary equivalent of 2 is 01
Replace 0’s instead of 1 and 1’s instead of 0’s
Final binary equivalent 10

SAMPLE INPUT 1:
3

SAMPLE OUTPUT 1:
0

SAMPLE INPUT 2:
12

SAMPLE OUTPUT 2:
3

SAMPLE INPUT 3:
3
	
SAMPLE OUTPUT 3:
0

SAMPLE INPUT 4:
34

SAMPLE OUTPUT 4:
29

SAMPLE INPUT 5:
9

SAMPLE OUTPUT 5:
6
'''

N  = int(input())
bin_cnb = bin(N).replace("0b","");k=''
for i in range(len(bin_cnb)):
	if(bin_cnb[i] == '0'):k+='1'
	else:k+='0'
print(int(k,2))
