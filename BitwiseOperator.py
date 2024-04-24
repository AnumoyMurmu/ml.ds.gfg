####
Bitwise Operators
EasyAccuracy: 49.22%Submissions: 25K+Points: 2
Three 90 Challenge Extended On Popular Demand! Don't Miss Out Now 

banner
Bitwise operators are useful when we want to work with bits. Here, we'll take a look at them.

Given three positive integers a, b, and c. Your task is to perform some bitwise operations on them as given below:
1. d = a ^ a
2. e = c ^ b
3. f = a & b
4. g = c | (a ^ a)
5. h = ~e
Note: ^ is for xor. The working of bitwise operators can be found here.

Example:

Input:
a = 4
b = 8
c = 2
Output:
0
10
0
2
-11
Constraints:
1 <= A, B, C <= 106
#####

soln:
#User function Template for python3
def bitWiseOperation(a, b, c):
    # code here
    
 
    print(a ^ a)
    print(c ^ b)
    print(a & b)
    print(c | (a ^ a))
    print(~(c ^ b))


