# 108.将有序数组转换为二叉搜索树(递归)
# 选择数组的中点，该点左边作为左子树，右边作为右子树
# 结束条件：数组为空
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    if not nums:
        return None
    mid = len(nums) // 2
    tree = TreeNode(nums[mid])
    tree.left = self.sortedArrayToBST(nums[0:mid])
    tree.right = self.sortedArrayToBST(nums[mid+1:len(nums)])
    return tree