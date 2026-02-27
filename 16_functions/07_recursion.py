"""
Topic: Python Recursion
Date: 2026-02-27
Concept Covered:
- Python Recursion
"""

# What is Recursion?
# Recursion is when a function calls itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# 
 # Example: A simple recursive function that counts down from 5:

def countdown(n):
    if n <= 0:
      print("Done!")
    else:
      print(n)
      countdown(n - 1)

countdown(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# Done!

# Base case and Recursive Case

# Every recursive function must have two parts:
    # 1. A base case - A condition that stops the recursion
    # 2. A Recursive case - The function calling itself with a modified argumenr

# Without a base case, the function would call itself forever, causing a stack overflow error.

# Example : 

def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
# Output: 120
# The base case is crucial. Always make sure your recursive function has a condition that will eventually be met.

# When Do We Use Recursion?
# 1. Mathematical Problems
     # Factorial
     # Fibonacci
     # Power calculation
     # GCD

# 2. Tree Structures (VERY IMPORTANT in DSA)
     # Trees are naturally recursive.

# Examples:

    # Binary Tree traversal (DFS)

    # Inorder, Preorder, Postorder

    # Height of tree

# Because:
    # Each node contains smaller trees (left subtree + right subtree)

# 3. Divide and Conquer Algorithms

# Algorithms like:

    # Merge Sort

    # Quick Sort

    # Binary Search

# They divide the problem into smaller parts.

# 4. Backtracking Problems

# Very important for interviews:

    # N-Queens

    # Sudoku solver

    # Maze problems

    # Subsets & permutations

# Benefits:
    # Cleaner code
    # More readable
    # Less code

# Drawbacks:
    # Can be less efficient
    # Can be more memory-intensive
    # Can be more complex to debug
    # If stack overflow is possible: 