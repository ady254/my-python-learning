"""
Problem: 3sum
given nums = [-1, 0, 1, 2, -1, -4]
find all unique triplets whose sum is 0

this problem teaches us how two pointer + sorting work together
"""
# step by step approch

# step 1: why sorting? because two pointer work on a sorting array
# nums.sort()
# becomes: [-4, -1, -1,  0, 1, 2]
# now we use TWO POINTER 

# step 2: Think
# choose one number: i then --> left ->        <- right
# find two number satisfying:
# nums[i] + nums[left] + nums[right] == 0

# if i = 0 and nums[i] = -4
# what should left and right initially be?
# initially pointer would be at start index and end of the index
# left = i + 1
# right = len(nums) - 1
# if total < 0 we need larger sum
# left += 1 if total > 0 right -= 1

# core 3sum rule
# total < 0  → left++
# total > 0  → right--
# total == 0 → found triplet

# Why do you think we need to skip duplicate values when nums[i], nums[left], or nums[right] are repeated?

# ans: Skipping duplicates is mainly required to avoid returning duplicate triplets

# Two pointers → reduces the search from O(n³) to O(n²).
# Skipping duplicates → prevents duplicate answers.

##############CODE##################
nums.sort()
left = i + 1
right = len(nums) - 1

while left < right:
    total = nums[i] + nums[left] + nums[right] == 0
    if total < 0:
        left += 1
    elif total > 0:
        right -= 1

    else:
        # found triplets

# when : total == 0 we found a valid triplet
# step 1: save it --> result.append([nums[i], nums[left], nums[right]])
# step 2: move both pointers left += 1 and right -=1
# step 3: skip duplicates 
#while left < right and nums[left] == nums[left - 1]:
 #   left += 1

#while left < right and nums[right] == nums[right + 1]:
#    right -= 1




# correct code:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Fixed typo: 'contiue' -> 'continue'

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result