# 101.对称二叉树(递归）
# 结束条件：左右节点都为为空
# 对称条件：1.左节点的左子树与右节点的右子树对称
#           2.左节点和右节点相等
def isSymmetric(self, root: TreeNode) -> bool:
    if root is None:
        return True

    def ismirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        l = ismirror(left.left, right.right)
        r = ismirror(left.right, right.left)
        return left.val==right.val and l and r
    
    return ismirror(root.left, root.right)