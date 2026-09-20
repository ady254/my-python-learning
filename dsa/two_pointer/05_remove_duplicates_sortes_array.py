"""
Pattern: SLOW AND FAST POINTER

Problem 5: Remove Duplicates from Sorted Array
# input: [1, 1, 2, 2, 3]
# output: 3
# explanation: the array should be [1, 2, 3, _, _] and we return the length of the array with unique elements which is 3

"""
# NeW PATTERN : in this pattern we have two pointer one is slow pointer and other is fast pointer
# Idea
# fast → explores the array.
# slow → keeps track of where the next unique value should go.
# Because the array is sorted, duplicates are next to each other.
# code:
# Brute force:

from ast import List
def remove_duplicates_brute_force(nums):
    unique_elements = []
    for num in nums:
        if num not in unique_elements:
            unique_elements.append(num)
    return len(unique_elements)

#optimal approach:
def removeDuplicates(nums: List[int]) -> int:
        if not nums:
            return 0
        
        # 'i' keeps track of the position of the last unique element found
        i = 0
        
        # 'j' explores the rest of the array
        for j in range(1, len(nums)):
            # If we find a new unique element
            if nums[j] != nums[i]:
                i += 1          # Move the unique pointer to the next spot
                nums[i] = nums[j]  # Overwrite it with the new unique value
                
        # The number of unique elements is the index + 1
        return i + 1

