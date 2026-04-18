# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getNextDigit(n1, n2, carry):
            first = 0 if not n1 else n1.val
            second = 0 if not n2 else n2.val

            sum = first+second+carry
            digit = sum%10
            carry = sum // 10

            return (ListNode(digit), carry)

        head = ListNode(0)
        cur = head
        carry = 0
        while l1 or l2 or carry:
            pair = getNextDigit(l1, l2, carry)
            cur.next = pair[0]
            carry = pair[1]

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return head.next