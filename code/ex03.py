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
          
    def reverse(self, s):
      return s[::-1]
# Test program

print(Solution().longestPalindrome("tracecars"))
# racecar

print(Solution().longestPalindrome("banana"))
#Output: "anana"

print(Solution().longestPalindrome("million"))
#Output: "illi"

print(Solution().longestPalindrome("bob"))