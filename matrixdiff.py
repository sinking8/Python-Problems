'''
Matrix Difference
In a given matrix R*C, In each row the absolute difference between every element is the same. Display the row in which the row elements differ with the largest difference.

INPUT:
First line contains no of rows (R) and no of columns (C)
R lines contains elements of the matrix

OUTPUT:
First line contains the row with largest difference

CONSTRAINTS:
1<= R, C <= 10^3
1<= elements of a matrix <= 10^3

SAMPLE INPUT:
3 2
1 2
4 2
3 9

SAMPLE OUTPUT: 
3 9

EXPLANATION: 
R = 3
C = 2
The first row elements differ by 1 (2-1)	
The second row elements differ by 2 (4-2)
The third row elements differ by 6 (9-3)
The third row elements has the highest difference hence the third row is printed

SAMPLE INPUT 1:
3 3
1 2 3
2 4 6
9 6 3

SAMPLE OUTPUT1:
9 6 3

'''

R, C = map(int,input().split())
mx_arr,mx = [],0 
for _ in range(R):
	arr = list(map(int,input().split()))
	if(abs(arr[1]-arr[0])>mx):
		mx_arr = arr[:]
		mx     = arr[1]-arr[0] 

print(*mx_arr,sep=" ")