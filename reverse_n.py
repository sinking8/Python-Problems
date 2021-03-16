'''
Reverse N Integers
The program must accept N integers as the input. The program must reverse integers up to M and display the final altered integers.

INPUT:
First line of input contains N and M separated by a space
Second line of input contains the N integers separated by a space.

OUTPUT:
Display the final N integers in reverse order

CONSTRAINTS:
1 <= N <= 10^3

SAMPLE INPUT:
6 2
10 22 30 14 51 60

SAMPLE OUTPUT: 
22 10 30 14 51 60

EXPLANATION: 
N = 2
Hence the first 2 elements 10 and 22 are reversed
The final output would be 22 10 30 14 51 60

SAMPLE INPUT 1:
5 4
1 2 3 4 5

SAMPLE OUTPUT 1:
4 3 2 1 5

SAMPLE INPUT 2:
5 5
1 2 3 4 5

SAMPLE OUTPUT 2:
5 4 3 2 1

SAMPLE INPUT 3:
5 0
1 6 3 2 6

SAMPLE OUTPUT 3:
1 6 3 2 6

SAMPLE INPUT 4:
3 2
1 2 3

SAMPLE OUTPUT 4:
2 1 3

SAMPLE INPUT 5:
4 3
1 2 3 5

SAMPLE OUTPUT 5:
3 2 1 5

'''
N, M = map(int,input().split())
arr = list(map(int,input().split()))
print(*arr[:M][::-1],sep=" ",end=" ")
print(*arr[M:],sep=" ")
