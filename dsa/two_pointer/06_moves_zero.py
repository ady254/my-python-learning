"""
Problem: Move all zeros to the end of the array while maintaining the relative order of the non-zero elements.
Example: 
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
Think: this is a slow + fast pointer problem ,
slow point: to the position where the non-zero element should be placed
fast pointer: iterate through the array.


"""
# slow = 0
# fast = 0
# what should we do when fast reaches 1?
# swap the element at the fast pointer with the element at the slow pointer
# increment the slow pointer
# nums[slow] = nums[fast]
# slow +=
# array become : [1, 1, 0, 3, 12]

# brute force code

def move_zero(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    for i in range(count, len(nums)):
        nums[i] = 0
    return nums

print(move_zero([0, 1, 0, 3, 12]))


# optimal solution

def move_zero(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    return nums

print(move_zero([0, 1, 0, 3, 12]))


# Interview byte

