# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = ((v1+v2+carry) // 10, (v1+v2+carry) % 10)
            #or carry, val = divmod((v1+v2+carry), 10)
            n.next = n = ListNode(val);
        return result

l1 = current = ListNode(2)
current.next = ListNode(4)
current = current.next
current.next = ListNode(3)
l2 = curr = ListNode(5)
curr.next = ListNode(6)
