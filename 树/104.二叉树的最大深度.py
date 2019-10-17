# 104.二叉树的最大深度(递归)
# 返回左子树和右子树的最大深度+1
# 结束条件：节点为空，返回0
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    depth_left = self.maxDepth(root.left)
    depth_right = self.maxDepth(root.right)
    return max(depth_left, depth_right) + 1
