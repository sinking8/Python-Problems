'''
Next Greater Number – Same Digits
A number N is passed as the input. The program must print the next greater number with the same digits.

INPUT:
First Line contains the value of N.

OUTPUT:
First line will contain the next greater number with the same digits.

CONSTRAINTS:
1 <= N <= 10^3

SAMPLE INPUT:
12

SAMPLE OUTPUT: 
21

EXPLANATION: 
Maximum Number which can be constructed with ‘2’ and ‘1’.

SAMPLE INPUT 1:
195

SAMPLE OUTPUT 1:
591

SAMPLE INPUT 2:
123

SAMPLE OUTPUT 2:
321

SAMPLE INPUT 3:
9843

SAMPLE OUTPUT 3:
9843

SAMPLE INPUT 4:
35212

SAMPLE OUTPUT 4:
53221

SAMPLE INPUT 5:
8709

SAMPLE OUTPUT 5:
9870

'''
N = str(input())
N_arr = [int(N[i]) for i in range(len(N))]
N_arr.sort();N_arr = N_arr[::-1]
print(''.join([str(no) for no in N_arr]))