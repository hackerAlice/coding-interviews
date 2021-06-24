#!/usr/bin/python3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dsf(r: TreeNode):
            if r.left:
                parents[r.left.val] = r
                dsf(r.left)
            if r.right:
                parents[r.right.val] = r
                dsf(r.right)

        parents = dict()
        visited = dict()
        parents[root.val] = None
        dsf(root)

        while p:
            visited[p.val] = True
            p = parents[p.val]

        while q:
            if visited.get(q.val, False):
                return q
            q = parents[q.val]

        return None


if __name__ == "__main__":

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)

    print(Solution().lowestCommonAncestor(root, root.left.left, root.right.right).val)