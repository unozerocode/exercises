class Solution:
    def isValid(self, s):
        return Solution().balanced(s)

    def balanced(self, s):
        if s == "": return True
        complement = []
        for c in s:
            #print(f"Examining {c}")
            if Solution().isOpening(c):
                complement.append(Solution().flip(c))
                #print(f"Pushed {Solution().flip(c)} Complement {complement}")
            elif Solution().isClosing(c):
                if len(complement) == 0: return False
                p = complement.pop()
                if p == c:
                    #print(f"Popped {c} as expected")
                    continue
                else :
                    #print(f"Popped {p}, bad match, expecting {c}")
                    return False
        if len(complement) > 0:
            #print(f"Ran out of input expecting {complement}")
            return False 
        else:
            return True       
            
    def isOpening(self, bracket):
        open_brackets = ["(", "[", "{"]
        return bracket in open_brackets

    def isClosing(self, bracket):
        close_brackets = [")", "]", "}"]
        return bracket in close_brackets

    def flip(self, bracket):
        if bracket == "(" : 
            return ")"
        elif bracket == "[" :
            return "]"
        elif bracket == "{" :
            return "}"
        elif bracket == ")":
            return "("
        elif bracket == "]":
            return "["
        elif bracket == "}":
            return "{"
        else:
            return ""

# Test Program
s = "()(){(())" 
print(f"Testing {s} Expecting False")
assert(Solution().isValid(s) == False)

s = ""  
print (f"Testing {s} Expecting True")
assert(Solution().isValid(s))

s = "([{}])()"
print (f"Testing {s} Expecting True")
assert(Solution().isValid(s))