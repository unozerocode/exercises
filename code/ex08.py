#You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.


def two_sum(list,k):
    print(f"Checking for two digits in {list} to add up to {k}")
    for i, m in enumerate(list):
        for j, n in enumerate(list):
            if (i == j): continue
            if (m+n == k): 
                print(f"{m} + {n} = {m+n}")
                return True 
            
        
    return False


print("Expecting True")
print (two_sum([4,7,1,-3,2], 5))
