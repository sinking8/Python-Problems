'''
Karim the shop owner of Karim-Kebabs is so fond of UPPER-KEBAB-CASE that his menu items are named in such a way 
that it follows UPPER- KEBAB-CASE and doesn’t follow any other cases. N items are placed in Karim-Kebabs with different cases. 
Print no of items which follow UPPER- KEBAB-CASE

INPUT:
In first line no of items ‘N’ must be taken as input
In second the food items in UPPER-KEBAB-CASE must be taken as input

OUTPUT:
Total No of valid UPPER-KEBAB-CASE values must be displayed

CONSTRAINTS:
I<=N<=10^5
	
SAMPLE INPUT:
3
KEBAB-JUICE-egg

SAMPLE OUTPUT: 
2

EXPLANATION: 
Three items are ordered which are ‘KEBAB’ , ‘JUICE’ and ‘egg’ but in the given input ‘KEBAB’ and ‘JUICE’ follow given type case and ‘egg’ doesn’t follow. Hence 2 is displayed

SAMPLE INPUT 1:
2
Egg-olives
OUTPUT:-
0

'''
N =  int(input())
c =  0
wrd = list(map(str,input().split('-')))

for w in wrd:
	if(w.upper() == w and w[0].isalpha()):
		c+=1

print(c)