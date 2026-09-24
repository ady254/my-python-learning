"""
Problem: container with most water
height = [1,8,6,2,5,4,8,3,7]
height = [1,8,6,2,5,4,8,3,7]

We choose two positions to form a container.

L                       R
↓                       ↓
[1, 8, 6, 2, 5, 4, 8, 3, 7]

The area is:

area = width × shorter_height

So:
area = (right - left) * min(height[left], height[right])
"""
# Approach 1: Brute force approach

def max_area_brute_force(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
    return max_area


# Approach 2: Two pointer approach
def max_area_two_pointer(height):
    max_water = 0
    left = 0
    right = len(height) - 1
        
    while left < right:
        # Calculate current width
        width = right - left
        # Calculate current area using the shorter line
        current_water = width * min(height[left], height[right])
            
        # Keep track of the maximum water found so far
        max_water = max(max_water, current_water)
            
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
                
    return max_water


