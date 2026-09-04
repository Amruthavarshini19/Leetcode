# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(node, min_val, max_val):
            if node is None:
                return 0
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            current_diff = max_val - min_val
            left = dfs(node.left, min_val, max_val)
            right = dfs(node.right, min_val, max_val)
            return max(current_diff, left, right)
        return dfs(root, root.val, root.val)
        