'''
Increment and Decrement Digits
Given an integer N,
Increment the digits at even position and Decrement the digits at odd position of integer N, Display the updated integer.

INPUT:
The integer N is given as input

OUTPUT:
Display the updated integer	

CONSTRAINTS:
1 <= N <= 10^3

SAMPLE INPUT:
13

SAMPLE OUTPUT: 
4

EXPLANATION: 
The digits present in odd position are 1.  Hence they are decremented (1->0)
The digits present in even position are 3. Hence they are incremented (3->4).
The final updated integer would be 4

SAMPLE INPUT 1:
24

SAMPLE OUTPUT 1:
15

SAMPLE INPUT 2:
1234

SAMPLE OUTPUT 2:
325

SAMPLE INPUT 3:
234343

SAMPLE OUTPUT 3:
143434

SAMPLE INPUT 4:
12324254

SAMPLE OUTPUT 4:
3233345

SAMPLE INPUT 5:
123531

SAMPLE OUTPUT 5:
32622

'''
N = str(input())
k = ''
for i in range(len(N)):
	if(i%2 == 0):
		k = k + str(int(N[i]) - 1)
	else:
		k = k + str(int(N[i]) + 1)
print(int(k))