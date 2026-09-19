"""
Two Pointers approach: in this approach we use two pointers to traverse the array
Question: Why we use two pointer which problem does two pointer approach solves?
ans: core reason: it reduces the time complexity from O(n^2) to O(n)
example: find a pair in a sorted array whose sum is equal to a given target value
arr = [1, 2, 3, 4, 5] and target = 6
If i use brute force method then it takes O(n^2) because it check every number with every other number
But with "TWO POINTER APPROACH" 
put one pointer at the start of index 0 which is left pointer and other pointer at end of index right
left = 0 and right = 4
sum = arr[left] + arr[right] = 1 + 5 = 6 this are the pair which sum is equal to target value

"""
# TWO POINTER PATTERNS

# 1. OPPOSITE DIRECTION
# 2. SAME DIRECTION  
# 3. SLIDING WINDOW


