class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if (l1.next == None) and (l2.next == None): 
        csum = l1.val + l2.val + c
        carry = 0
        if csum > 9:
            csum = csum - 10
            carry = 1
            carryNode = ListNode(carry)
            resultNode = ListNode(csum)
            resultNode.next = carryNode
            return resultNode
        else:
            resultNode = ListNode(csum)
            return resultNode
    elif (l1.next == None):
        result = Solution().addTwoNumbers(l1.val, c)
        return result
    elif (l2.next == None):
        result = Solution().addTwoNumbers(l2.val, c)
        return result
    else:
        csum = l1.val + l2.val + c
        carry = 0
        if csum > 9:
            csum = csum - 10
            carry = 1

        result = ListNode(csum)
        result.next = Solution().addTwoNumbers(l1.next, l2.next, carry)
        return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print ("Expecting 7 0 8")
result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val)
  result = result.next

# 3 4 8 + 9 9 9 = 1 3 4 7
# 8 -> 4 -> 3
# 9 -> 9 -> 9
# 7 4 3 1 
print("Expecting 7 4 3 1")
l1 = ListNode(8)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
