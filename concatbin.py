'''
Concatenate Binary- Largest Integer
The program must accept two integers X and Y as a input. 
The program must print the largest possible integer which is formed by concatenating the binary representation of X and Y as input.

INPUT:
The first line contains X and Y separated by a space.

OUTPUT:
The first line contains the largest integer which is formed by concatenating the binary representation of X and Y

CONSTRAINTS:
1<=X, Y <= 10^5

SAMPLE INPUT:
7 10

SAMPLE OUTPUT: 
122

EXPLANATION:
The binary representation of 7 is 111.
The binary representation of 10 is 1010.
The largest possible integer formed is 122 and its binary representation is 1111010. 

SAMPLE INPUT 1:
8 5

SAMPLE OUTPUT1:
88

'''
def find_decimal(val):
	deci = 0
	for i in range(len(val)-1,-1,-1):
		deci += int(val[i])*(2**(len(val)-i))
	return deci


X, Y = map(int,input().split())
X_bin, Y_bin =  bin(X).replace("0b",""), bin(Y).replace("0b","");

if(find_decimal(X_bin+Y_bin)>find_decimal(Y_bin+X_bin)):
	print(find_decimal(X_bin+Y_bin)//2)
else:
	print(find_decimal(Y_bin+X_bin)//2)

