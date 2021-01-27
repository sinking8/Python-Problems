'''
Array Rotation
Given an array of M elements, the program must rotate the array according to the given input; if the input is L then the array should be left rotated if its R then the array should be right rotated

INPUT:
The first line includes the size of the array M
The second line includes the elements of the array separated by space.
The third line includes the commands separated by a space.

OUTPUT:
The first line must display the elements of the array after the rotations

CONSTRAINTS:
1<= M <= 10
0<= elements of the array M <= 10^3

SAMPLE INPUT:
3
1 2 3
L R R

SAMPLE OUTPUT: 
3 1 2

EXPLANATION: 
Initial array: 1 2 3
L: 2 3 1
R: 1 2 3
R: 3 1 2
Final Output: 3 1 2

SAMPLE INPUT 1:
4
6 4 2 1
L R R R

SAMPLE OUTPUT1:
2 1 6 4

'''

M = int(input())
arr = list(map(int,input().split()))
commands  = list(map(str,input().split()))
for command in commands:
	if command == 'L':
		arr.append(arr.pop(0))
	else:
		arr.insert(0,arr.pop(-1))

print(*arr,sep=" ")