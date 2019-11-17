class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def to_s(self):
        if self.val == None:
            return "None"
        else:
            if self.next == None:
                next_node = "None"
            else:
                next_node = str(self.next.val)

            return f"{str(self.val)}->{next_node}"

    # Function to print the list
    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
            
        print(output)

    # Iterative Solution
    def reverseIteratively(self):
        ret = None
        previous_node = None
        current_node =  self
        next_node = None
        
        while current_node != None:
            next_node = current_node.next
            ret = current_node
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        return ret

    # Recursive Solution      
    def reverseRecursively(self):
        def rec(node, prev):
            #print(f"Processing {node.to_s()}")
            next_node = node.next
            
            if next_node == None:
                node.next = prev
                #print(f"Terminating with {node.to_s()}")
                #print(f"returning {node.to_s()}")
                return node
            else:
                node.next = prev
                #print(f"swap pointers {node.to_s()}")
                return rec(next_node, node)

        return rec(self, None)

# Test Program
# Initialize the test list: 
def init_test():
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail
    return testHead

testHead = init_test()
print("Initial list: ")
testHead.printList()

rev_iter = testHead.reverseIteratively()
print("List after iterative reversal, expecting 0 1 2 3 4")
rev_iter.printList()

testHead = init_test()
print("Initial list: ")
testHead.printList()
print("List after recursive reversal: Expecting  0 1 2 3 4")
rev_recurse = testHead.reverseRecursively()
rev_recurse.printList()
