'''
Unit Digit Ascending
The program must accept two integers as the input. The program must sort the two integers in ascending order based on their unit digit and print them as the output. If the unit digits are same then sort the two integers in descending order and print them as the output.

INPUT:
Input contains the numbers separated by a space

OUTPUT:
Display the numbers sorted according to their unit digit

CONSTRAINTS:
1<= numbers <= 10^3

SAMPLE INPUT:
57 102

SAMPLE OUTPUT: 
102 57

EXPLANATION: 
102 57 
2<7 hence 102 and 57 swapped

SAMPLE INPUT 1:
275 15

SAMPLE OUTPUT 1:
275 15

SAMPLE INPUT 2:
123 532

SAMPLE OUTPUT 2:
532 123

SAMPLE INPUT 3:
235 239

SAMPLE OUTPUT 3:
235 239

SAMPLE INPUT 4:
12 21

SAMPLE OUTPUT 4:
21 12

SAMPLE INPUT 5:
5 6

SAMPLE OUTPUT 5:
5 6

SOLUTION:
a, b = map(str,input().split())
if(int(a[-1])<=int(b[-1])):
	print(a,b,sep=" ")
else:
	print(b,a,sep=" ")

'''
a, b = map(str,input().split())
if(int(a[-1])<=int(b[-1])):
	print(a,b,sep=" ")
else:
	print(b,a,sep=" ")