'''
Country Capital
Input data containing N countries and their capital will be provided as input.
The program must then print the capital for a given country.

INPUT:
First line will contain the integer value N representing how many country-capital pairs.
Next N lines will contain the name of the country and the name of the capital as string values separated by a space.
The last line will contain the name of the country as a string value for which the capital is to be printed as output.

OUTPUT:
First line will contain the capital of the country. If the name of the country is Not found then NONE must be printed as output.

CONSTRAINTS:
2 <= N <=100

SAMPLE INPUT:
3
Austria Vienna
Armenia Yerevan
Croatia Zagreb
Austria

SAMPLE OUTPUT: 
Vienna

EXPLANATION: 
As capital of Austria is Vienna hence Vienna is displayed

SAMPLE INPUT 1:
2
Armenia Yerevan
Iran Tehran
Japan

SAMPLE OUTPUT 1:
NONE

SAMPLE INPUT 2:
3
Austria Vienna
Armenia Yerevan
Croatia Zagreb
Armenia

SAMPLE OUTPUT 2:
Yerevan

SAMPLE INPUT 3:
3
Iran Tehran
China Beijing
Chile Santiago
Japan

SAMPLE OUTPUT 3:
NONE

SAMPLE INPUT 4:
2
USA DC
UK London
UK

SAMPLE OUTPUT 4:
London

SAMPLE INPUT 5:
USA DC
London

SAMPLE OUTPUT 5:
NONE

'''
N = int(input())
d = dict()
for _ in range(N):
	a,b = map(str,input().split())
	d[a] = b
country = input().strip()
if(country in d.keys()):print(d[country])
else:print("NONE")
