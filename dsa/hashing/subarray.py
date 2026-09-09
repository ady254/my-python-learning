"""
Problem Hash map + Prefix sum
Goal: can prefix sum + hashmap help me find a previous prefix tht gives me the target?

"""
# What is prefix sum in simple word?
# A prefix sum is a running total of numbers in an array where each spot stores the sum of all previous numbers plus itself
 
# Imagine you have an array of numbers: [1, 2, 3, 4, 5]
# To make a prefix sum array, you add each new number to the running total so far
# eg:
# Index 0: 1
# Index 1: 1 + 2 = 3
# Index 2: 1 + 2 + 3 = 6
# Index 3: 1 + 2 + 3 + 4 = 10
# Index 4: 1 + 2 + 3 + 4 + 5 = 15

# Your new prefix sum array is [1, 3, 6, 10, 15]
# Why Use It?
# Save Time: Instead of adding numbers over and over again to find a range sum, you do it once in the beginning
# Fast Queries: If you want the sum of numbers from index 1 to 3 (2 + 3 + 4 = 9), you just subtract two numbers from your pre-made array (10 - 1 = 9) instead of looping through them
