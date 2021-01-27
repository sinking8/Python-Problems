'''
Array Left Rotation
Given an array of M elements, the program must apply N left rotation to the array according 

INPUT:
The first line includes the size of the array M
The second line includes the elements of the array separated by space.
The third line includes the N

OUTPUT:
The first line must display the elements of the array after the rotations

CONSTRAINTS:
1<= M <= 10
0<= elements of the array M <= 10^3

SAMPLE INPUT:
3
1 2 3
2

SAMPLE OUTPUT: 
3 1 2

EXPLANATION: 
Initial array: 1 2 3
L: 2 3 1
L: 3 1 2
Final Output: 3 1 2

SAMPLE INPUT 1:
4
1 2 3 4
5

SAMPLE OUTPUT1:
2 3 4 1

'''
M = int(input())
arr = list(map(int,input().split()))
for _ in range(int(input())):
	arr.append(arr.pop(0))
print(*arr,sep=" ")