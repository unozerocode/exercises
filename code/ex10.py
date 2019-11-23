#You are given an array of integers in an arbitrary order.
#Return whether or not it is possible to make the 
# array non-decreasing by modifying at most 1 element 
# to any value.

#We define an array is non-decreasing if 
# array[i] <= array[i + 1] holds for every 
# i (1 <= i < n).

def nondecreasing(ary):
    for i,n in enumerate(ary):
        if (i==0): continue
        if (n < ary[i-1]): return False
        
    return True

def attempt_modify(lst):
    for i,n in enumerate(lst):
        if (i==0): continue
        if (lst[i-1] > n) :
            # Try modifying i, then i-1
            saved = lst[i]
            lst[i] = lst[i-1]
            if nondecreasing(lst):
                print(f"Fixed with Right Alternative at {i}")
                return True
                
            else:    
                lst[i] = saved
                lst[i-1] = saved 
                if nondecreasing(lst):
                    print(f"Fixed with Left Alternative at {i}")
                    return True
                else:
                    return False
    return False

def check(lst):
    if nondecreasing(lst): 
        return True
    else:
        return attempt_modify(lst)


print("Expecting True")
print(check([13, 4, 7]))
# True
print("Expecting False")
print(check([5,1,3,2,5]))
# False
print("Expecting True")
print(check([1,1,0,3,4,5]))