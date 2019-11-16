class Solution: 
    def getRange(self, arr, target):
    # Find indices of first and last occurrences that of target element
        first = -1
        last = -1
        idx = 0
        for i in arr:
            if i == target:
                if first == -1:
                    first = idx
                else:
                    last = idx
            idx += 1
      
        return [first, last]
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print("Expecting [1,4]")
print(Solution().getRange(arr, x))
# [1, 4]

arr = [1,3,3,5,7,8,9,9,9,15]
x = 9
print("Expecting [6,8]")
print(Solution().getRange(arr,x))

arr = [100, 150, 150, 153]
x = 150
print("Expecting [1,2]")
print(Solution().getRange(arr,x))

arr = [1,2,3,4,5,6,10]
target = 9
print("Expecting [-1, -1]")
print(Solution().getRange(arr, x))