'''
Jim’s walk to greatness
Jim went for a vacation to lulu land. While he was strolling the land he saw a staircase which seems not to end. He asked about that to a person nearby. He mentioned that the staircase could take a person to greatness. But it was not that easy, the no of steps that he could walk depends on his power of wisdom and how much he is determined to attain greatness. Find out the no of steps that Jim could traverse.

INPUT:
The first line includes no of test cases T.
The first line of each test case T includes no of steps visible to Jim’s view.
The second line includes the height’s of each step. 

OUTPUT:
Display no of steps that he could traverse in each line.

CONSTRAINTS:
1 <= T, height of the steps, 10^3

SAMPLE INPUT:
1
1 2 3 5 1

SAMPLE OUTPUT: 
4

EXPLANATION: 
No of test cases : 1
Height of each step increases up to 4th step. After the 4th step the height no longer increases (the height of the 5th step: 1). 
Hence no of steps that Jim could traverse to reach the maximum height is 4.

SAMPLE INPUT 1:
2
1 2 3 1
5 6 7 4

SAMPLE OUTPUT 1:
3
3

SAMPLE INPUT 2:
3 
1 2 3 4 4 5 2
4 5 7 8 2 1
1 2 3 3 2 1

SAMPLE OUTPUT 2:
6
4
4

SAMPLE INPUT 3:
1
1 1 1 2 2 1

SAMPLE OUTPUT 3:
5

SAMPLE INPUT 4:
2
1 2 3 3 4 5 56 2
4 5 6 6 2 1

SAMPLE OUTPUT 4:
7
4

SAMPLE INPUT 5:
1
1 2 3 4 3 3 3 1

SAMPLE OUTPUT 5:
4

'''
T = int(input())
for _ in range(T):
	steps = list(map(int,input().split()))
	for i in range(len(steps)-1):
		if(steps[i]>steps[i+1]):break
	print(i+1)