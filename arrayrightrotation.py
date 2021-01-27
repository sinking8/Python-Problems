'''
Array Right Rotation
Given an array of M elements, the program must apply N right rotation to the array.

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
2 3 1

EXPLANATION: 
Initial array: 1 2 3
R: 3 1 2
R: 2 3 1
Final Output: 2 3 1

SAMPLE INPUT 1:
4
1 2 3 4
5

SAMPLE OUTPUT1:
4 1 2 3

'''
M = int(input())
arr = list(map(int,input().split()))
for _ in range(int(input())):
	arr.insert(0,arr.pop(-1))
print(*arr,sep=" ")