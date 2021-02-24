'''
Fibonacci Words
The program must accept the integer N as the input. The program must print the first N Fibonacci words formed by repeating them in the same way as generating Fibonacci Numbers. The first term and the second term of the Fibonacci words is ‘a’ and ‘b’.

INPUT:
Input contains N which denotes the number of Fibonacci terms.

OUTPUT:
Display N Fibonacci Terms separated by a space.

CONSTRAINTS:
1 <= N <= 25

SAMPLE INPUT:
6

SAMPLE OUTPUT: 
A ab ba bab babba babbabab

EXPLANATION: 
Here N = 6 and first two terms in the Fibonacci words are ‘a’ and ‘b’.
The 3rd term in the Fibonacci words is ba (“b”+”a”).
The 4th term in the Fibonacci words is bab(“ba” +”b”)
The 5th term in the Fibonacci words is babba(“bab” + “ba”)
The 6th term in the Fibonacci words is babbabab(“babba” + “bab”).

SAMPLE INPUT 1:
2

SAMPLE OUTPUT 1:
a b

SAMPLE INPUT 2:
5

SAMPLE OUTPUT 2:
a b ba bab babba

SAMPLE INPUT 3:
6

SAMPLE OUTPUT 3:
a b ba bab babba babbabab

SAMPLE INPUT 4:
8

SAMPLE OUTPUT 4:
a b ba bab babba babbabab babbababbabba babbababbabbababbabab

SAMPLE INPUT 5:
1

SAMPLE OUTPUT 5:
a

'''
N = int(input())
a,b = 'a', 'b'
print(a,b,end=" ",sep=" ")
s = None
for _ in range(N-2):
	s = b + a
	print(s,end=" ")
	a = b
	b = s
	

