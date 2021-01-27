'''
Football Selection
The head coach for the football team requires several players for the upcoming tournament. He asked N students to stand in increasing height order to make his selection process easier. But the students had a different plan; some of the students were not interested in playing football so they placed themselves in such a manner that the coach would not see them. Display the positions of the students who tried to escape from the coach?

INPUT:
First line includes total number of students N
Second line includes the heights of the students
OUTPUT:
Display the positions of the students who tried to escape

CONSTRAINTS:
3<= N <= 10^3

SAMPLE INPUT:
4
3 9 2 1

SAMPLE OUTPUT: 
3 4

EXPLANATION: 
The heights of the students are 3 9 2 1
The 3rd student has placed himself behind 2nd student, who is taller than him so he won’t be visible,
Similarly the 4th person has placed himself behind 3rd person
Hence 3 4 is printed

SAMPLE INPUT 1:
5
4 2 6 1 3

SAMPLE OUTPUT1:
2 4 5

'''

N = int(input())
students = list(map(int,input().split()))
pos = []
for i in range(1,N):
	if(max(students[:i])>students[i]):pos.append(i+1)
print(*pos,sep=" ")