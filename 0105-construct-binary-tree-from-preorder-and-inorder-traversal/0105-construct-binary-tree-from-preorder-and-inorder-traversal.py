# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Time Complexity: O(n^2)
        # Reason:
        # - for every recursive call, inorder.index(root_val) can take O(n)
        # - slicing also costs extra
        #
        # Space Complexity: O(n)
        # Reason:
        # - recursion stack
        # - sliced subarrays are created

        if not preorder or not inorder:
            return None

        # first value in preorder is root
        root_val = preorder[0]
        root = TreeNode(root_val)

        # find root position in inorder
        mid = inorder.index(root_val)

        # build left subtree
        root.left = self.buildTree(
            preorder[1:mid + 1],
            inorder[:mid]
        )

        # build right subtree
        root.right = self.buildTree(
            preorder[mid + 1:],
            inorder[mid + 1:]
        )

        return root
        