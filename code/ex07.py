#Input: [3, 3, 2, 1, 3, 2, 1]
#Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
    #print(f"Sorting {nums}")
    sorted = False
    swap = False
    #print(f"Sorting array of length {len(nums)}")
    while not sorted:
        for index,n in enumerate(nums):
            # Sort pair
            #print(f"Inspecting index {index}")
            #print(f"Comparing [{index}]({nums[index]}) and [{index+1}]({nums[index+1]})")
            if (nums[index] > nums[index+1]):
                #print("Swap")
                temp = nums[index]
                nums[index] = nums[index+1]
                nums[index+1] = temp
                swap = True
                #print(f"After Swap [{index}]({nums[index]}) and [{index+1}]({nums[index+1]})")
            
            if (index==len(nums)-2):
               if not swap: sorted = True
               #print(f"hit limit at {index}, swap {swap},  sorted {sorted}")
               swap = False
               break
    return nums

print("Expecting  [1, 1, 2, 2, 3, 3, 3]")
print (sortNums([3, 3, 2, 1, 3, 2, 1]))