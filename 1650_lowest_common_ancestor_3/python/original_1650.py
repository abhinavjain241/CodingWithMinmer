class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p_start: Node, q_start: Node) -> Node:
        p = p_start
        q = q_start
        while p != q:
            if p.parent:
                p = p.parent
            else:
                p = q_start

            if q.parent:
                q = q.parent
            else:
                q = p_start

        return p