"""
Problem 4: Container with Most Water
Given: height = [1,8,6,2,5,4,8,3,7]
we choose two positions to form a container

area = width x shorter_height
area = (right - left) * min(height[left], height[right])

Imagine with Most Water
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

          |                       |
          |                       |
          |                       |
          |   |                   |
          |   |                   |
          |   |       |           |
          |   |   |   |       |   |
          |   |   |   |   |   |   |
          |   |   |   |   |   |   |
   
          L                       R


Rule:
left height < right height
        ↓
     left++

left height > right height
        ↓
     right--

left height == right height
        ↓
     move both
"""
# Code:
from ast import List
def maxArea(self, height: List[int]) -> int:
        max_water = 0     # in this line we initialize max_water to 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate current width
            width = right - left
            # Calculate current area using the shorter line
            current_water = width * min(height[left], height[right])
            
            # Keep track of the maximum water found so far
            max_water = max(max_water, current_water)    # in this line we update max_water with the maximum of current_water and max_water
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

# Interview Questions:
# 1. Why do we move the pointer pointing to the shorter line?
# ans: 
# Because if we move the pointer pointing to the taller line, the width will decrease and the height will either decrease or stay the same, so the area will either decrease or stay the same. 
# But if we move the pointer pointing to the shorter line, the width will decrease but the height might increase, so the area might increase.  
# 2. What if height[left] == height[right]? Which pointer should we move?
# ans: 
# In this case, we can move either pointer, but the optimal approach is to move both pointers. 