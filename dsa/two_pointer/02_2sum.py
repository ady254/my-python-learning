"""
Problem: TWO SUM
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
#Code:

def two_sum(nums: list[int], target: int) -> list[int]:
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left +1, right + 1]

        elif total < target:
            left += 1

        else: 
            right -= 1

# Remember this rule:
# total == target -> answer
# total < target -> left ++
# total > target -> right --

# Question : Why does total < target mean we move left?
# Because the array is sorted, so moving left right gives us a larger number.

# If nums[left] + nums[right] > target, why can't we move left instead?
# because moving the pointer left gives smaller value so we need to move are left pointer towards right that so right -1


