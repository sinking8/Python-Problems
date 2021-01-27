'''
Maximum Repeating Count
Given an array of N integers, the program must find the value which repeats in maximum number of times and print the number. In case of ties, choose the smallest number and print it.

INPUT:
First line will contain the array of integers of length N separated by one or more spaces

OUTPUT:
The most repeated integer value in the array

CONSTRAINTS:
1<= N <= 30
1<= integers in the array <= 100

SAMPLE INPUT:
10 20 30 20 30 10 30 20

SAMPLE OUTPUT: 
20

EXPLANATION: 
Both 20 and 30 repeat 3 times. But 20 is smaller than 30 hence 20 is printed

SAMPLE INPUT 1:
1 2 3 5 9 2 9 6 9

SAMPLE OUTPUT1:
9
'''

arr = list(map(int,input().split()))
uniq = list(set(arr))
mini,cnt = uniq[0],arr.count(uniq[0])
uniq.pop(0)
for no in uniq:
	if(arr.count(no)>=cnt):
		if((mini>no and arr.count(no) == cnt) or arr.count(no)>cnt):
			mini = no
			cnt = arr.count(no)
print(mini)