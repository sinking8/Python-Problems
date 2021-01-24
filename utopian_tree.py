'''
UTOPIAN TREE

The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 3 meter.
A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

Period Height
0          1
1          2
2          5
3          10
4          13
5          22

INPUT:
The first line contains an integer t, the number of test cases.                                                                                                              T lines each contain a integer n , the number of cycles for that test case.

OUTPUT:
Display the height of the tree after the given number of cycles.

CONSTRAINTS:
1<=t<=20
0<=n<=50

SAMPLE INPUT:
3
0
1
4

SAMPLE OUTPUT: 
1
2
13

EXPLANATION:
There are 3 test cases.
In the first case (n = 0), the initial height (h = 1) of the tree remains unchanged.                                       In the second case (n = 1), the tree doubles in height and is 2 meters tall after the spring cycles.                             In the third case (n = 4), the tree doubles its height in spring (n = 1, H = 2), and grows another 3 meter after summer (n = 2, H = 5), then doubles after the next spring (n = 3, H = 10), and grows another 3 meters after summer (n = 4, H = 13). Thus, at the end of 4 cycles, its height is 13 meters.

SAMPLE INPUT 1:
2
10
3

SAMPLE OUTPUT1:
125 
10

'''

def utopianTree(n):
    init_case = int(1)
    for i in range(n):
        if(i%2 == 0):
            init_case*=2;
        else:
            init_case+=3;
    return init_case

if __name__ == '__main__':
    t = int(input())
    results = []
    for t_itr in range(t):
        n = int(input())
        results.append(utopianTree(n))      
    print(*results,sep="\n")