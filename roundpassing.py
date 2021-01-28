'''
Round Passing
M girls and N boys of a playschool formed a circle were placed randomly.  Someone in the circle in the position P would start passing the passing of the ball continues until the ball reaches the person who started it. The boys had a tendency to break the rules whereas the girls didn’t. The boys would skip n persons corresponding to their position and pass to the n+1th person. For example if a boy is in the second position then he skips two children and passes to the third child. Displays no of passes require reaching the person who started it.

INPUT:
First line includes no of girls (M) and no of boys (N)
Second line includes the order in which boys and girls are placed
-	Even number represents a boy and odd number represents a girl.
-	Example: 1 2 3 6; In the example boys are places in positions 2 and 4 whereas the girls are placed in positions 1 and 3
Third line includes the position of the person who is starting to pass

OUTPUT:
Displays no of passes require to end the game.

CONSTRAINTS:
1<= M, N <= 10^5
1<= P <= M+N

SAMPLE INPUT:
3 0
1 3 5
2

SAMPLE OUTPUT: 
3

EXPLANATION: 
No of Girls (M): 3
No of Boys (N):  0

Positions: 1 3 5
Starting Player Position: 2
There are only 3 girls but no boys in the game. So there won’t be any cheating in the game.

PASS = 1
Initially the ball would be given to the second player who is 3 as she is a girl she would pass it 5

PASS = 2
5 is also a girl so she would pass it to the next person who is 1 

PASS = 3
1 is also a girl she passes it to 3 who started the game.
Hence 3 passes where required to complete the game.

SAMPLE INPUT 1:
3 1 
1 2 3 5
3

SAMPLE OUTPUT1:
3

SAMPLE INPUT 2:
5 0
1 3 5 7 9
3

SAMPLE OUTPUT 2:
5

SAMPLE INPUT 3:
3 1
4 1 3 5
2

SAMPLE OUTPUT 3:
4

SAMPLE INPUT 4:
3 1
1 3 5 7
2

SAMPLE OUTPUT 4:
4 

SAMPLE INPUT 5:
6 1
1 2 3 5 7 9 11
4

SAMPLE OUTPUT 5:
6

'''

M,N = map(int,input().split())
positions = list(map(int,input().split()))
P = int(input())
passes,strt_pos = 0, P
while(True):	
	strt_pos%=(M+N)
	if(positions[strt_pos-1]%2 == 0):
		strt_pos+=strt_pos
	
	else:
		strt_pos+=1

	passes+=1
	if(P == strt_pos):
		break

print(passes)