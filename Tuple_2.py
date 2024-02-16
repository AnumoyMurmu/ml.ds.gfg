# Tuple 2
# MediumAccuracy: 86.68%Submissions: 948+Points: 4
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# You are given a tuple numbers that contains a A.P sequence integer. You need to calculate the next three sequences of numbers and return the whole sequence in a tuple.

# Example 1:

# Input:
# numbers = ( 1 ,5, 9, 13, 17 )
# Output: 
# 1 5 9 13 17 21 25 29
# Explanation: It's an increasing sequence by 4. So, the next three numbers are 17+4= 21,  21+4=25, 25+4=29.
# Example 2:

# Input:
# numbers = (3, 1 ,-1, -3 ,-5 ,-7 )
# Output:
# 3  1  -1  -3  -5  -7  -9  -11  -13
# Explanation:  It's an decreasing sequence by 2.  So, the next three numbers are  -7-2=-9, -9-2=11, -11-2=-13
# Your Task: 
# Write the code to create a tuple of whole sequence. Finally, return the tuple. The driver code will print the returned tuple.

# soln:

#User function Template for python3

def sequence(numbers):
    
    
    # code here to return tuple containing whole sequences
    seq=numbers[1]-numbers[0]
    arr=[]
    for i in numbers:
        arr.append(i)
    last=arr[-1]
    
    # 1st sequence
    first=int(last)+seq
    arr.append(first)
    
    # 2nd sequence
    second=int(first)+seq
    arr.append(second)
    
    # 3rd sequence
    third=int(second)+seq
    arr.append(third)
    
    return tuple(arr)
    