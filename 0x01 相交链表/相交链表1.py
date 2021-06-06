"""
方法一：哈希集合
思路和算法

判断两个链表是否相交，可以使用哈希集合存储链表节点。

首先遍历链表 \textit{headA}headA，并将链表 \textit{headA}headA 中的每个节点加入哈希集合中。然后遍历链表 \textit{headB}headB，对于遍历到的每个节点，判断该节点是否在哈希集合中：

如果当前节点不在哈希集合中，则继续遍历下一个节点；

如果当前节点在哈希集合中，则后面的节点都在哈希集合中，即从当前节点开始的所有节点都在两个链表的相交部分，因此在链表 \textit{headB}headB 中遍历到的第一个在哈希集合中的节点就是两个链表相交的节点，返回该节点。

如果链表 \textit{headB}headB 中的所有节点都不在哈希集合中，则两个链表不相交，返回 \text{null}null。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_node = headA
        b_node = headB

        node_a_list = []

        while a_node:
            node_a_list.append(a_node)
            a_node = a_node.next

        while b_node:
            if b_node in node_a_list:
                return b_node

        return None