
#two sum problem 

# q1. nums = [2, 7, 11, 13] and target = 9 find the index from which add up gives the targte value 

seen = {}  # empty dict

for i, num in enumerate(nums):
    complement = target - num      # calculate the complement as target - num
    if complement in seen:        # then i check that complement is already in the map, if i found i return both indices
        return [seen[complement], i]     
    
    
    seen[num] = i    #  otherwise i it store the current number and index

# Interview Approch :
# I use a hashmap to store the each number along with its index, for every number, I calculate its complement as target - num
# then i check whether that complement is already in the map. If it is i found the pair and return both indices 
# otherwise, i store the current number and its index
# this gives O(n) average time and 0(n) space