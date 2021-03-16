'''
Adding reversed numbers
A pair of numbers (X and Y) will be passed as input. The program must reverse the numbers and find the sum S. Then the sum S must be reversed and printed as output.
-	If any leading zeroes are obtained while reversing any of the numerical values they should be discarded.

INPUT:
First line will contain the value of X
Second line will contain the value of Y

OUTPUT:
The first line will contain the sum S

CONSTRAINTS:
0 < X, Y < 10000

SAMPLE INPUT:
24
1

SAMPLE OUTPUT: 
34

EXPLANATION: 
23 when reversed are 42. So 42 +1 = 43
When 43 are reversed it is 32 and hence 34 is the output.

SAMPLE INPUT 1:
1
2

SAMPLE OUTPUT 1:
3

SAMPLE INPUT 2:
12
3

SAMPLE OUTPUT 2:
42

SAMPLE INPUT 3:
34
2

SAMPLE OUTPUT 3:
54

SAMPLE INPUT 4:
5
12

SAMPLE OUTPUT 4:
71

SAMPLE INPUT 5:
32
12

SAMPLE OUTPUT 5:
53

'''
X = str(input());Y = int(input())
X = int(X[::-1]) + Y
print(str(X)[::-1])