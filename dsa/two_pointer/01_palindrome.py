"""
Problem 1: Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

"""
#Code:
def isPalindrome(s: str) -> bool:
    # convert all uppercase letters to lowercase letters and removing all non-alphanumeric characters
    s = "".join(filter(str.isalnum, s)).lower()
    
    # two pointer approach
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

