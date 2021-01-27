'''
Applicants Group - Purchase Amount
In a University, N students have enrolled for their course of study. The name of each student and his/ her course are passed as input to the program. The program must group the students based on the courses selected by the students. The program must print the course and the names of the students belonging to each group as the output.

INPUT:
The first line contains N
The next N lines each containing the student name and the course taken separated by a space

OUTPUT:
The line(s), each containing the courses and the student(s) name separated by a space.

CONSTRAINTS:
1<= N <= 50
1<= length of the student name, Course Name <= 20

SAMPLE INPUT:
3
Raj CSE
Kumar CSE
Tom EEE

SAMPLE OUTPUT: 
CSE Raj Kumar
EEE Tom

EXPLANATION: 
The courses are CSE and EEE in the given Input.
There are two students who are enrolling for CSE and one student who is enrolling for EEE.
Hence they are grouped according to the course taken and displayed

SAMPLE INPUT 1:
4
Ajay MECH
Kingston ECE
Arjun MECH
John ECE

SAMPLE OUTPUT1:
MECH Ajay Arjun
ECE Kingston John

'''
d = dict()
for _ in range(int(input())):
	name, group = map(str,input().split())
	if group in d:
		d[group].append(name)
	else:
		d[group] = [name]


for key,pairs in d.items():
	print(key,end=" ")
	print(*pairs,sep=" ")