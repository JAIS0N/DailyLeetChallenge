# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(h)
        # n = number of nodes, h = height of tree

        max_sum = float("-inf")  # stores global answer

        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0

            # ignore negative paths
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # path using this node as center
            current_sum = node.val + left + right

            # update global max
            max_sum = max(max_sum, current_sum)

            # return best path to parent (only one side)
            return node.val + max(left, right)

        dfs(root)
        return max_sum