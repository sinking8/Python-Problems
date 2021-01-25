'''
SAM’S BUNNY 
Sam took his bunny for a hopping competition which happened in his community. The course consists of N steps and was made in such a way that the obstacles will be placed in random order by the jury. The input for obstacles would be the position where they are placed if they are not placed then the value -1 would be given as input. The only rule of the competition is that the bunny should cover the same number of steps in each hop, if the bunny gets caught in an obstacle it needs to revert and start from the beginning. The maximum no of steps that the bunny could cover in each hop will be ‘M’. Display the no of steps per hop with which the bunny would succeed, if it’s not possible then display -1. 

INPUT:
1st line contains the number of steps N of the course
2nd line contains the positions of the obstacles
3rd line contains maximum steps per hop M

OUTPUT:
Display no of steps per hop if possible else display -1

CONSTRAINTS:
1<=M, N <= 10^5

SAMPLE INPUT:
3
-1
3

SAMPLE OUTPUT: 
1 3

EXPLANATION: 
There are no obstacles in the course as the input is -1

hops =  1
0->1->2->3
Hence hops = 1 is possible

hops = 2
0->2->4
The ending is not 3 , the bunny hops an additional step, Hence hops = 2 is not possible

hops = 3
0->3
The ending is 3, thus hops = 3 is possible

SAMPLE INPUT 1:
6
3
2

SAMPLE OUTPUT1:
2

'''

N = int(input())
obstacles =  list(map(int,input().split()))
M = int(input())
hops = []
for hop in range(1,M+1):
	flag = True
	for i in range(1,N,hop):
		if (i-1) in obstacles:
			flag = False
			break
	if(flag==True and N%hop == 0):hops.append(hop)
print(*hops,sep=" ")