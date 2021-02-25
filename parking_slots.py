'''
Parking Slots – Vehicles Count
There are several vehicles parked in a matrix format. But the vehicle can be of varying size. A parked vehicle is represented by one or more ‘V’ along a given row. An empty parking slot is represented using a dot (‘.‘).

INPUT:
First line contains R (no of rows) and C (no of columns) separated by a space.
Next R lines contain the parking slots status.

OUTPUT:
Output includes no of cars in parking slots.

CONSTRAINTS:
1 <= R, C <= 10^5

SAMPLE INPUT:
3 5
V V .V .
. . . V .
. V V V V

SAMPLE OUTPUT: 3 5
4

EXPLANATION: 
In the first row, there are 2 vehicles parked.
In the second row, there is one vehicle parked.
In the third row, there is one vehicle parked.
So totally there are 4 vehicles.

SAMPLE INPUT 1:
2 2
V V
. .

SAMPLE OUTPUT 1:
1

SAMPLE INPUT 2:
2 3
V . .
V V V

SAMPLE OUTPUT 2:
2

SAMPLE INPUT 3:
1 5
V . V . V

SAMPLE OUTPUT 3:
3

SAMPLE INPUT 4:
2 3
. . .
. . .

SAMPLE OUTPUT 4:
0

SAMPLE INPUT 5:
3 3
. . .
V V V
V . V

SAMPLE OUTPUT 5:
3

'''
R,C  = map(int,input().split())
cnt = 0
for _ in range(R):
	arr = list(map(str,input().split()))
	flag = False
	for i in range(len(arr)):
		if(arr[i] == 'V'):
			if(flag == False):
				cnt+=1
				flag = True

		else:
			flag = False


print(cnt)
