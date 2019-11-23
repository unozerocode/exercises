def singleNumber(nums):
    
    for i,m in enumerate(nums):
        pair_found = False
        for j,n in enumerate(nums):
            #print(f"i{i}, j{j} searching for duplicate of {m}")
            if(i == j): continue # Don´t compare to itself
            if(m == n): 
                pair_found = True; 
                #print(f"Pair found for {m} at {i},{j}")
                break # pair found, go to next
        
        if not (pair_found): 
            #print(f"Found single integer {m}")
            return m

print("Expecting 1")
print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
