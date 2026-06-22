# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.rslt = None
        self.connector = None
        
        def reverse(node, count):
            if count == k-1:
                if not self.rslt:
                    self.rslt = node
                if self.connector:
                    self.connector.next = node
                return node
            
            reverse(node.next, count+1).next = node
            return node

        cur_head = head
        cur_node = head
        counter = 0

        while True:
            if counter == k:
                chunk = reverse(cur_head, 0)

                self.connector = chunk
                chunk.next = cur_node
                cur_head = cur_node
                
                counter = 0
            
            if not cur_node:
                break
            
            counter += 1
            cur_node = cur_node.next

        return self.rslt

