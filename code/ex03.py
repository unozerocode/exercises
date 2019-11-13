class Solution: 
    def longestPalindrome(self, s):
        longest = ""
        substrings = Solution().substrings(s)
        for sub in substrings:
          revsub = sub[::-1]
          revindex = s.find(revsub)
          if revindex >= 0 :
              if len(revsub) > len(longest):
                longest = revsub
        return longest
    
    def substrings(self,s):
      r = []
      for i in range(0, len(s)):
        for j in range(i+2,len(s)+1):
          #print(f"{i},{j} {s[i:j:1]}")
          r.append(f"{s[i:j:1]}")
      return r
          
# Test program

print("Expecting racecar")
print(Solution().longestPalindrome("tracecars"))
# racecar

print("Expecting anana")
print(Solution().longestPalindrome("banana"))
#Output: "anana"

print("Expecting illi")
print(Solution().longestPalindrome("million"))
#Output: "illi"

print("Expecting bob")
print(Solution().longestPalindrome("bob"))