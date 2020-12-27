"""
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans_head = ListNode()
        curr_ans_node = ans_head
        
        carry = 0
        
        while l1 != None and l2 != None:
            current_sum = carry + l1.val + l2.val
            carry = current_sum // 10
            current_sum = current_sum % 10
            
            curr_ans_node.next = ListNode(current_sum)
            curr_ans_node = curr_ans_node.next
            
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            current_sum = carry + l1.val
            carry = current_sum // 10
            current_sum = current_sum % 10
            
            curr_ans_node.next = ListNode(current_sum)
            curr_ans_node = curr_ans_node.next
            
            l1 = l1.next
        
        while l2 != None:
            current_sum = carry + l2.val
            carry = current_sum // 10
            current_sum = current_sum % 10
            
            curr_ans_node.next = ListNode(current_sum)
            curr_ans_node = curr_ans_node.next
            
            l2 = l2.next
        
        if carry != 0:
            curr_ans_node.next = ListNode(carry)
        
        return ans_head.next