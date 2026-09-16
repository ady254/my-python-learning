"""
Sub array : A subarray is a contiguous part of an array.
Problem Hash map + Prefix sum
Goal: can prefix sum + hashmap help me find a previous prefix that gives me the target?

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
"""
================Interview==========why you use prefix and hashmap=========
We need to find contiguous subarrays with a target sum. 
Prefix Sum lets us calculate a subarray sum using two prefix sums, 
and HashMap lets us quickly find how many previous prefix sums can form k with the current prefix.

"""
#Smallest Missing Integer Greater Than Sequential Prefix Sum
"""
Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] 
with a sum of 6. 6 is not in the array, 
therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
"""
#code:
from typing import List
class Solution:
    def missingInteger(self, nums: List [int]) -> int:
        prefix_sum = nums[0]
        i = 1

        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            prefix_sum += nums[i]
            i += 1
# convert nums into set
        num_set = set(nums)

# find the smallest missing integer >= prefix_sum
        while prefix_sum in num_set:
            prefix_sum += 1

        return prefix_sum
# workthrough:
"""
nums[i] == nums[i - 1] + 1

nums[i]--> The number at the current position.

nums[i - 1] --> The number directly before it.

nums[i - 1] + 1 --> What the current number should be if the sequence increases by 1.

== --> Compares if the current value matches that expected consecutive value.
 nums = [1, 2, 3, 2, 5]
 At i = 1: nums[1] is 2, nums[0] is 1.2 == 1 + 1 True (sequence continues: 1, 2)
 At i = 2: nums[2] is 3, nums[1] is 2.3 == 2 + 1 True (sequence continues: 1, 2, 3)
 At i = 3: nums[3] is 2, nums[2] is 3.2 == 3 + 1 False (sequence breaks, loop stops)
"""

"""
Problem 2 complete solution
subarray sums divisible by K 
nums = [4, 5, 0, -2, -3, 1]
k = 5
pattern: prefix sum + hashmap
we're looking for contigous sub arrays

formula: Rule 1 if : current_prefix % k == previous_prefix % k
         Rule 2 then: (current_prefix - previous_prefix) % k == 0

nums = [4, 5, 0, -2, -3, 1]
k = 5
prefix sums: 4, 9 , 9, 7, 4, 5
4 % 5 = 4
9 % 5 = 4
9 % 5 = 4
7 % 5 = 2
4 % 5 = 4
5 % 5 = 0
notice: 4 appears multiply times
Therefore the subarray between those two prefix sums has a sum divisible by k
hashmap: {remainder : count}
"""


