class TreeNode(object):
    def __init__(self):
        self.val = None
        self.left = TreeNode()
        self.right = TreeNode()


class Solution(object):
    def constructMaximumBinaryTree(self,nums):
        if len(nums) == 0:
            return None
        M = max(nums)
        root = TreeNode()
        root.val = M
        pos = nums.index(M)
        root.left = self.constructMaximumBinaryTree(nums[:pos])
        root.right = self.constructMaximumBinaryTree(nums[pos:])
        return root



