'''
Matrix Problem
You are given a square matrix of size NxN. 
Calculate the absolute difference of the sums of the two main diagonals.

INPUT:
The first line contains the value of N
The next lines will contain the N values separated by space

OUTPUT:
Display the absolute difference of the sums across the two main diagonals.

CONSTRAINTS:
1<= N <= 20

SAMPLE INPUT:
2
10 9
4 22

SAMPLE OUTPUT: 
19

EXPLANATION: 
The sum along the first diagonal is 10 + 22 = 32
The sum along the second diagonal is 9 + 4 = 13
The absolute difference is 32-13 = 19

SAMPLE INPUT 1:
3
1 2 3
4 5 6
9 10 11

SAMPLE OUTPUT 1:
0

SAMPLE INPUT 2:
4
1 2 3 4
6 4 2 1
10 2 4 5
12 54 2 0

SAMPLE OUTPUT 2:
11

SAMPLE INPUT 3:
4
10 12 12 2
4 5 6 6
2 4 5 6
1 23 5 6

SAMPLE OUTPUT 3:
13

SAMPLE INPUT 4:
3
10 20 30
60 3 2
1 5 7

SAMPLE OUTPUT 4:
14

SAMPLE INPUT 5:
4
1 2 3 4
4 3 2 1
5 6 7 8
8 7 6 5

SAMPLE OUTPUT 5:
4

'''
N = int(input())
arr = []
for _ in range(N):arr.append(list(map(int,input().split())))
main_diag = abs(sum([arr[i][i] for i in range(N)]) - sum([arr[i][N-i-1] for i in range(N)]))
print(main_diag)