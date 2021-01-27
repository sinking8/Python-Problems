'''
MinSum
Given two arrays A and B of equal size n, the task is to find the minimum value of A[0]*B[1] …. + A[n-1]*B[n-1], where shuffling of elements of arrays A and B is allowed. 

INPUT:
The first line of input contains an integer denoting the no of test cases T
The T test cases follow. 
Each test case consists of following inputs
The first line of the test case consists of size of the array N
The second and the third line consist of the data elements of the array A and B.

OUTPUT:
Display the minimum value of product of elements between two arrays A and B

CONSTRAINTS:
1<= T, N <= 50
1<= elements of the array <= 100

SAMPLE INPUT:
3
3 1 1
6 4 5

SAMPLE OUTPUT: 
23

EXPLANATION: 
Minimum value of the S = 1*6 + 1* 5 + 2 *4 = 23

SAMPLE INPUT 1:
5
6 1 9 5 4
3 4 8 2 4

SAMPLE OUTPUT1:
80
'''

for _ in range(int(input())):
	N = int(input())
	A = list(map(int,input().split()))
	B = list(map(int,input().split()))
	A.sort();B.sort()
	B = B[::-1]
	S  = sum([A[i]*B[i] for i in range(N)])
	print(S)