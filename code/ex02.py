class Solution:
  def lengthOfLongestSubstring(self,s):
      if len(s) == 0: return 0
      longest = 0
      current_longest = 0
      prev_c = ''
      for c in s:
        if c != prev_c:
            current_longest = current_longest+1
        else:
            if current_longest > longest:
                longest = current_longest
            current_longest = 1
            
        prev_c = c

      return longest


print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))