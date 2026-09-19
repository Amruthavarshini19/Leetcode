# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        def dfs(node):
            if node is None:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            take = node.val + left[1] + right[1]
            skip = max(left[0], left[1]) + max(right[0], right[1])
            return (take, skip)
        ans = dfs(root)
        return max(ans[0], ans[1])