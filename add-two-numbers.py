# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        curry = 0
        
        root = ans
        
        while l1 and l2:
            _sum = l1.val + l2.val + curry
            curry = _sum//10
            ans.next = ListNode(_sum %10)
            ans = ans.next
            l1, l2 = l1.next, l2.next
        
        while l1:
            _sum = l1.val + curry
            curry = _sum//10
            ans.next = ListNode(_sum %10)
            ans = ans.next
            l1 = l1.next 
        
        while l2:
            _sum = l2.val + curry
            curry = _sum//10
            ans.next = ListNode(_sum %10)
            ans = ans.next
            l2 = l2.next 
        
        while curry:
            ans.next = ListNode(curry %10)
            ans = ans.next
            curry = curry//10
            
        
        return root.next
