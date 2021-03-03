'''
String Binary Representation
The program must accept two string values S1 and S2 as the input. The string S1 always contains only 8 lower case alphabets representing 8 bits of a byte. For each character in the string S2, The program must find the binary representation (8 bits) of its ASCII value. Then the program must convert the binary representation of each character to string S1 based on the following conditions.
-	Replace each bit with the corresponding alphabet in S1. If it is 0, then the alphabet must be in lower case. Else the alphabet must be in upper case.
-	Final the program must display the string values obtained as the output.

INPUT:
The first line contains S1.
The second line contains S2. 

OUTPUT:
The output contains the string values obtained separated by a space.

CONSTRAINTS:
1 <= Length of S2  <= 10^5

SAMPLE INPUT:
Universe
Hello

SAMPLE OUTPUT: 
uNivErse uNIveRsE uNIvERse uNIvERSE

EXPLANATION: 
S1 = universe
S2 = Hello
ASCII value of H = 72 -> 01001000 -> uNIvErse
ASCII value of e = 101 -> 01100101 -> uNIveRsE
ASCII value of l = 108  -> 01101100 -> uNIvERse
ASCII value of l = 108  -> 01101100 -> uNIvERse
ASCII value of o = 111 -> 01101111 -> uNIvERSE 

SAMPLE INPUT 1:
abcdefgh
hello

SAMPLE OUTPUT 1:
aBCdEfgh
aBCdeFgH
aBCdEFgh
aBCdEFgh
aBCdEFGH

SAMPLE INPUT 2:
Facebook
jello

SAMPLE OUTPUT 2:
fACeBoOk
fACebOoK
fACeBOok
fACeBOok
fACeBOOK

SAMPLE INPUT 3:
Kingsman
kelps

SAMPLE OUTPUT 3:
kINgSmAN
kINgsMaN
kINgSMan
kINGsman
kINGsmAN

SAMPLE INPUT 4:
corporat
kilns

SAMPLE OUTPUT 4:
cORpOrAT
cORpOraT
cORpORat
cORpORAt
cORPorAT

SAMPLE INPUT 5:
calamari
sheet

SAMPLE OUTPUT 5:
cALAmaRI
cALaMari
cALamArI
cALamArI
cALAmAri

'''

S1 = input().strip()
S2 = input().strip()

for i in range(len(S2)):
	asc = bin(ord(S2[i])).replace("0b","0")
	for j in range(len(asc)):
		if(asc[j] == '0'):
			print(S1[j].lower(),end="")
		else:print(S1[j].upper(),end="")
	print()