"""
Problem: given an array of integers sorted in non-decreasing order, 
return an array of the squares of each number also sorted in non-decreasing order. 
Example: 
Input: [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Think: this is a slow + fast pointer problem , we can use two pointer approach 
left pointer: start from the beginning of the array
right pointer: start from the end of the array
compare the absolute values of the elements at the left and right pointers
if the absolute value of the element at the left pointer is greater than the absolute value of the element at the right pointer
place the square of the element at the left pointer at the end of the result array
increment the left pointer
else
place the square of the element at the right pointer at the end of the result array
decrement the right pointer

"""
    
def sortedSquares(nums):
    n = len(nums)
    result = [0] * n

    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1

        pos -= 1

    return result