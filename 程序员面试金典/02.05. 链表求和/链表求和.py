#!/usr/bin/python3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = None
        temp_node = None
        cur = 0

        while l1 and l2:
            if not ans:
                ans = ListNode((cur + l1.val + l2.val) % 10)
                temp_node = ans
            else:
                temp_node.next = ListNode((cur + l1.val + l2.val) % 10)
                temp_node = temp_node.next
            cur = (cur + l1.val + l2.val) // 10

            l1 = l1.next
            l2 = l2.next

        while l1:
            temp_node.next = ListNode((cur + l1.val) % 10)
            temp_node = temp_node.next
            cur = (cur + l1.val) // 10
            l1 = l1.next

        while l2:
            temp_node.next = ListNode((cur + l2.val) % 10)
            temp_node = temp_node.next
            cur = (cur + l2.val) // 10
            l2 = l2.next

        if cur:
            temp_node.next = ListNode(1)

        return ans