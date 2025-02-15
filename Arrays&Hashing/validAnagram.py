# Valid Anagram
# Solved 
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):            # Check if the length of two strings is equal
        return False
        
      countS, countT = {}, {}
      
      for i in range(len(s)):
        # .get returns the value present in dict or returns 0 if no value is present
        countS[i] = 1 + countS.get(s[i], 0)
        countT[i] = 1 + countT.get(t[i], 0)

      for j in countS:            # c is the key
        if countS[j] != countT.get(j, 0):
          return False
          
      return True
