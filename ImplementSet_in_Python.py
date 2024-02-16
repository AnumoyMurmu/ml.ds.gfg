# Implement Set in Python
# EasyAccuracy: 87.44%Submissions: 3K+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# A set is an unordered collection of items where every element is unique and must be immutable, but set is mutable. You cannot access an element of set using indexing or slicing, but you can update the set.

# Some important functions in Set in Python:
# add(): Adds an element to the set.
# clear(): Removes all elements from the set
# discard(): Removes an element from the set if present.
# remove(): Removes an element from the set. If the element is not present, it raises error.
# pop(): Removes and returns an arbitary set element. Raise error if the set is empty.
# union(): Returns the union of sets in a new set
# update(): Updates the set with the union of itself and others
# len(): Return the length of set.
# sorted(): Return a new sorted list from elements in the set.
# sum(): Return the sum of all elements in the set.

# Let's implement these methods through a question. Given Q queries to do some operation on Set, the task is to perform all the queries in the Set as given below:
# a. i element: Adds element to the set.
# b. r element: Remove element from set.
# c. s: Find sum of elements in set. Returns the sum of elements in Set.

# Constraints:
# 1 <= S[i] <= 104

# Your Task:
# The task is to complete the functions given in user text area according to the query.

# soln:
#User function Template for python3

# Function to insert
# no return should be there, and no print statement
def insert(s, element):
    # Your code here
    s.add(element)
    
    
    

# Function to remove element from set
# No return and nothing to print
def remove_from_set(s, element):
    # Your code here
    
    s.discard(element)
    
    
    
# Function to find sum of elements in set
# return value should be there as sum
def sum_set(s):
    # Your code here
    
    return sum(s)
    
    