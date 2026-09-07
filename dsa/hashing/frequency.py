# 2nd Pattern -- Frequency: How many times --> Hash Map
# Question: Valid Anagram

# An anagram means:
# Both strings contain exactly the same characters with exactly the same frequencies.

# s = "anagram"
# t = "nagaram" 
# return True; otherwise False
# before solving think as 1% coder

#Q1. What is the brute-force idea?

#One simple approach is:
"""
Sort both strings
anagram → aaagmnr
nagaram → aaagmnr
If the sorted strings are equal:
True
Otherwise:
False
Python:
sorted(s) == sorted(t)
Complexity
If each string has n characters:
Sorting → O(n log n)
So:
Time  → O(n log n)
Space → depends on implementation, generally O(n)
"""
# this work but, we do better:
"""
Q2. What information do we actually need?
We don't really care about the order of characters.
We care about:
How many times does each character appear?
For:
anagram
we get:
a → 3
n → 1
g → 1
r → 1
m → 1
For:
nagaram
we get:
n → 1
a → 3
g → 1
r → 1
m → 1
The maps contain the same information.
Therefore:
frequency → Hash Map

"""
"""
# 3. Which pattern?

We had:
A) Existence ---> Have I seen this? -> Hash Set eg: contains duplicate
B) Frequency --> How many times? -> Hash Map eg: Valid anagram
C) Index mapping
D) Complement --> What do I need, and where did I see it? --> hash map eg: two sum
Correct: B — Frequency
The key question is:
"How many times does each character occur?"
Whenever you hear:
1.frequency
2.count
3.occurrences
#how many times
#your brain should immediately consider:
#Hash Map
"""

#Q4. Why can't a Set alone solve it ?
"""
consider: 
s = "ab"
t = "aab"

using set: s = set('ab') give {"a", "b"} and t = {"a", "b"} they give equal but t has two "a" they are not anagrams
therefore, A Set loses frequency information because duplicates are automatically discarded.

SET
→ preserves existence
→ loses frequency

MAP
→ preserves key + information
→ can store frequency

"""

# final code for the DSA question: s = "anagram"
# t = "nagaram" 
# return True; otherwise False

def is_anagram(s, t):
    if len(s) != len(t):     # checked if both s and t len are equal or not, if not return false
        return False

    count_s = {}       # created empty dict to store the values for s 
    count_t = {}       # created empty dict to store the values for t

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1    # here count_s.get(char, 0) + 1  check if char exits return thr current value otherwise map with default value zero not throw error

    for char in t:
        count_s[char] = count_t.get(char, 0) + 1

    return count_s == count_t      # if both are equal in number return True


# clearner  we can also write this in python using Counter
# code: 
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
