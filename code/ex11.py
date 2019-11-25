class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def toDOT(self) : 
        ret = f"{self.value}"

        if (self.left != None): 
            ret += f"->"
            ret += self.left.toDOT()

        if (self.right != None): 
            ret += f"{self.value}->" + self.right.toDOT()

        if (self.left == None and self.right == None):
            ret += f";\n"

        return ret

    # Floor - greatest int less than or equal to k
    # Ceil - least int greater than or equal to k
    def findCeilingFloor(self, k, floor=None, ceil=None):
        print(f"FindCeiling {k}")

        if (floor == None):
            if (self.value < k):
                floor = self.value 
        else:
            if (self.value < k and self.value > floor):
                floor = self.value

        if (ceil == None):
            if (self.value > k):
                ceil = self.value
        else:
            if (self.value > k and self.value < ceil):
                ceil = self.value
        
        print(f"Node {self.value} k: {k} Floor {floor} Ceil {ceil}")

        print("Left subtree")
        if (self.left != None) : 
            (floor,ceil) = self.left.findCeilingFloor(k, floor, ceil)
        print(f"Floor {floor} Ceil {ceil}")
        
        print("Right subtree")
        if (self.right != None) : 
            (floor,ceil) = self.right.findCeilingFloor(k, floor, ceil)

        print(f"Floor {floor} Ceil {ceil}")
        
        return (floor, ceil)

def buildDOT(node):
    res = "digraph G {"
    res += node.toDOT()
    res += "}"
    return res 

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 

root.left.left = Node(2) 
root.left.right = Node(6) 

root.right.left = Node(10) 
root.right.right = Node(14) 

print("Expecting (4,6)")
print(root.findCeilingFloor(5))

#print(buildDOT(root))
# (4, 6)