'''
2.Prime Binary Tree
A binary tree must be constructed with the root node as N and children nodes should be in such a manner that the left node holds N-1 and the right node holds N-2 This must be continued until a prime number is reached. Find the sum of the leaf nodes.

Boundary Condition(s):
1<=N<=10000

Input Description:
The first line contains N

Output Description:
Output the sum of prime leaf nodes.

Sample Input 1 :
6

Sample Output 1:
3

Problem Explanation:
N takes the value 6 the left node will take a value 5(N-1) and right node will take a value(N-2) the left node terminates and the right node continues to expand and terminates with children nodes 3 and 2
S = 2 + 3 + 5 = 10
Hence 10 is printed

Test Case 1: 
Input :  5
Output: 5

Test Case 2:                                                                                                                               Input :  10
Output: 41

Test Case 3: 
Input :  89
Output: 89

Test Case 4: 
Input :  6
Output: 10

Test Case 5: 
Input :  9
Output: 24 

'''
class BinaryTree:

	def __init__(self,value):
		
		self.value = value
		self.left  = None
		self.right = None

def prime(no):

	if(no == 2 or no ==1 or no ==3):return 1

	for i in range(2,(no//2)+1):

		if no%i == 0:return 0

	return 1

def bin(N):

	if(prime(N) == 1):
		return N

	elif(prime(N) == 0):
		
		node = BinaryTree(N)
		node.left =N-1
		node.right = N-2
		return( bin(node.left)+bin(node.right))

N = int(input())
print(bin(N))