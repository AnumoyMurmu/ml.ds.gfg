# Tuple 1
# EasyAccuracy: 93.05%Submissions: 954+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# You are given a tuple numbers that contains integers. You need to return a tuple containing doubles of given numbers.

# Example 1:

# Input:
# numbers = (4,5,1,2,3,5)
# Output: 
# 8,10,2,4,6,10
# Explanation: multiplied number by 2.
# Example 2:

# Input:
# numbers = (3,1,4,7,2,6,4)
# Output:
# 6,2,8,14,4,12,8
# Explanation: multiplied number by 2.
# Your Task: 
# Write the code to create a tuple containing double the given tuple. Finally, return the tuple. The driver code will print the returned tuple.

# soln:

#User function Template for python3

def doubleTup(numbers):
    
    #Write your code to create a tuple that 
    #holds 2*number 
    #Finally retrn the tuple
    ans=[]
    for item in numbers:
        ans.append(2*item)
        
    return tuple(ans)
    
    #   for item in numbers:
    #     ans = tuple(2*item)
        
    # return ans
    