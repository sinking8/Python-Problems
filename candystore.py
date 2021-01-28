'''
Candy Store

Jack and Jill are planning to meet at a candy store.
They always like to pool their money and buy candies.
Jack does not buy the same flavor that Jill does.
Jack and Jill always try to spend all their money and enjoy their time to fullest.
Given a list of prices for the flavors of candies, select the two candies that will cost most of their money they have. 

INPUT:
The first line contains the number of test cases T.
The next T set of lines describe a visit. Each visit is describes as follows.
The integer M, the amount of money they pooled.
The integer N, the number of flavors offered at the time.
N integers denoting the cost of each flavor.

OUTPUT:
For each test case:
print two space-separated integers denoting the indices of the two flavors purchased in ascending order.

CONSTRAINTS:
1<=T<=50
2<= M, N<=10^3
1<= cost of each flavor <= 10^3

SAMPLE INPUT:
1
4
3
1 3 2

SAMPLE OUTPUT: 
1 2

EXPLANATION: 
No of trips = 1
Total money pooled (M) = 4
The cost of different flavors (N flavors) is 1 2 3
Flavors 1 and 2 have a total cost 1+3 = 4, hence 1 and 2 is displayed

SAMPLE INPUT 1:
2
10
3
5 2 1
5
4
1 2 3 5

SAMPLE OUTPUT1:
1 2
2 3

SAMPLE INPUT 2:
2
10
3
5 9 1
20 2
10 10

SAMPLE OUTPUT 2:
2 3
1 2

SAMPLE INPUT 3:
1
10
2
9 1

SAMPLE OUTPUT 3:
1 2

SAMPLE INPUT 4:
1
20
3
9 8 2

SAMPLE OUTPUT 4:
1 2

SAMPLE INPUT 5:
 3
50
4
20 30 19 30
40
2
10 20
20
6
2 2 4 3 23 30

SAMPLE OUTPUT 5:
1 2
1 2
3 4


'''
T = int(input())
for _ in range(T):
	M = int(input())
	N = int(input())
	costs = list(map(int,input().split()))
	a,b,mx = 0, 0, 0
	for i in range(N):
		for j in range(i+1,N):
			s = costs[i]+costs[j]
			if(M-s>=0 and mx<s):
				mx = s
				a,b = i+1, j+1



	print(a,b,sep=" ")

