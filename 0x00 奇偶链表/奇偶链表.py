#!/usr/bin/python3


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def odd_even_list(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head

        # odd, even 分别表示指向奇点和偶数点指针
        # 其中head维持奇数链表，tail维持偶数链表
        odd, even = head, head.next
        tail = even

        current = even.next
        is_odd = True
        while current:
            if is_odd:
                odd.next = current
                odd = odd.next
            else:
                even.next = current
                even = even.next

            current = current.next
            is_odd = not is_odd

        if not is_odd:
            even.next = None

        odd.next = tail
        return head


if __name__ == '__main__':

    head = None
    cur = None
    for i in range(1, 6):
        if not head:
            head = ListNode(i)
            cur = head
        else:
            cur.next = ListNode(i)
            cur = cur.next

    Solution().odd_even_list(head)
