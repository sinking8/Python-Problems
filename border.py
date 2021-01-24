'''
In a given matrix of size R*C check whether the element N is present in the boundary display the top and the bottom element else display -1. 

INPUT:
First line will contain R and C.
R lines will contains the elements of the matrix
R+1 line contains the element N to be checked

OUTPUT:
Display the top and the bottom element of n if it’s not a border element. If it’s a border element display -1

CONSTRAINTS:
1 ≤ R, C, N ≤ 10^5

SAMPLE INPUT:
3 3
1 2 3
9 10 11
12 34 54
10

SAMPLE OUTPUT: 
2 34

EXPLANATION: 
The given no 10 is does not belong to the border element hence the top and bottom element is displayed which is 2 and 34
1 2 3
9 10 11
12 34 54

INPUT:
3 3
1 2 3
4 5 6
7 8 9
1

OUTPUT:
-1

INPUT:
4 4
1 2 3 4
9 10 11 12
6 7 8 0
5 18 23 20
7

OUTPUT:
10 18

'''
R, C, arr = map(int,input().split())
arr = []
for _ in range(R):arr.append(list(map(int,input().split())))
N = int(input())

arr_border  = [arr[i][0] for i in range(R)]
arr_border  = [arr[i][-1] for i in range(R)] + arr_border
arr_border  = [arr[0][i] for i in range(C)]  + arr_border
arr_border  = [arr[-1][i] for i in range(C)] + arr_border


if(N in arr_border):
	print("-1")

else:
	for i in range(R):
		if(N in arr[i]):
			inx = arr[i].index(N)
			print(arr[i-1][inx],arr[i+1][inx],sep=" ")
