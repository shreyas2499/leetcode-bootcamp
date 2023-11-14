
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        temp, ans = [], [[root]]
        while True:
            for i in range(len(ans[-1])):
                var = ans[-1][i]
                if var.left:
                    temp.append(var.left)
                if var.right:
                    temp.append(var.right)
                ans[-1][i] = var.val
            if not temp:
                return ans
            ans.append(temp)
            temp = []