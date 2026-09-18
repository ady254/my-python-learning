"""
Problem: Make Sum Divisible by P
nums = [3, 1, 4, 2]
p = 6

A subarray is defined as a contiguous, non-empty subsequence of the array. 

"""

# brute force solution 
from ast import List
def minSubarray(nums, p) -> int:
    n = len(nums)
    ans = n
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum % p == 0:
                ans = min(ans, j - i + 1)
    return ans if ans < n else -1

    #   Optimized solution 
    from ast import List

    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)     # we take total array sum which is 10 

        target = total % p    # because we want target element from the array which is 4 

        if target == 0:
            return 0

        remainder_index = {0: -1}  # intialised hashmap with 0 index and -1 value 

        prefix = 0                # initialized prefix sum to 0
        answer = len(nums)        # initialized answer to array length

        for i, num in enumerate(nums):
            prefix += num                # in this line we calculate prefix sum 

            current_remainder = prefix % p # in this line we calculate current remainder

            needed = (current_remainder - target) % p # in this line we calculate needed remainder

            if needed in remainder_index:               # in this line we check if needed remainder is in hashmap
                length = i - remainder_index[needed] # in this line we calculate length
                answer = min(answer, length)           # in this line we update answer with minimum length

            remainder_index[current_remainder] = i  # in this line we store current remainder and its index
        
        return answer if answer < len(nums) else -1 # in this line we return answer with minimum length if answer is less than 
                                                    # array length otherwise return -1 
   

###############Interview explaination ####################
"""
"I'm looking for a contiguous subarray whose sum has a particular remainder. 
Prefix Sum lets me express a subarray sum as the difference between two prefix sums,
and the HashMap lets me quickly find whether the required previous remainder has already appeared.
"""



        