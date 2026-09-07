"""
Problem : Group Anagrams
Given: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Expected: [
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]
how to trun a complicated object into hash map key
"""
# 1.Question first 
# eat
# tea
# ate
# Are they the same strings?
# no, but the contain same charachters

# Anagrams have identical character frequencies.

# 2. We nned a signature
# A signature is a representation that is the same for objects that belong to the same group.
# for eg:
# eat -> a1e1t1
# tea -> a1e1t1
# ate -> a1e1t1
# so three have different strings pointed same key

# how do we generate the signature?

# Apporch 1 sort each word
# eg: eat -> aet, tea -> aet, ate -> aet ---> by sorting we get same key i.e.. aet
# we use --> key = "".join(sorted(word))
# note: "".join() --> is a method used to glue a list of string together into one single string
# eg: word = ['h', 'i'] --> "".join(word) --> hi

# python implementation: we can use defaultdict 
# default dict: is a special type of dictionary that automatically assigns a default value to a key that does not exist yet
# eg : without default dict problem is:
# Imagine you are counting how many times different words appear in a list.
# Using a Regular DictionaryYou have to manually check if the word is already in your dictionary. If it isn't, you must set it to 0 first before you can add to it.
# code:
counts = {}
words = ["apple", "banana", "apple"]
for word in words:
    if word not in counts:
        counts[word] = 0 #manual check

    counts[word] += 1

# code:  
from collections import defaultdict

counts = defaultdict(int)  #'int' makes the default 0
words = ["apple", "banana", "apple"]

for word in words:
    counts[word] += 1   # No if-statement needed!


# group anagrams code will be:

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# let slow down the important line:
#groups[key].append(word)
# initially groups = {}   aet doesnt exit
# create [] append "eat"
# now {"aet": ["eat"]}
# complexity is nlogn
# for optimize solution

# we know 26 possible chars in english letters
count = [0] * 26
# problem is groups[count].append(word)
# no, list are mutable and unhasable
# so we convert into tuple --> hashable representation
# tuple(count)


# Optimized solution
from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        count = [0] * 26

        for char in word:
            index = ord(char) - ord('a')
            count[index] += 1

        key = tuple(count)

        groups[key].append(word)

    return list(groups.values())