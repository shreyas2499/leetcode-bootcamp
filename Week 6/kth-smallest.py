class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(root):
            if root is None:
                return []

            return inorder(root.left)+[root.val]+inorder(root.right)

        l=inorder(root)
        return l[k-1]
