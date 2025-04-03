from ...utils.treenode import TreeNode

class Solution:
    def lowestCommonAncestor(self, nodes: list[TreeNode], p_start: TreeNode, q_start: TreeNode) -> TreeNode:
        parent = {}
        for node in nodes:
            if node.left:
                parent[node.left] = node
            if node.right:
                parent[node.right] = node

        p = p_start
        q = q_start
        while p != q:
            if parent[p]:
                p = parent[p]
            else:
                p = q_start

            if parent[q]:
                q = parent[q]
            else:
                q = p_start

        return p