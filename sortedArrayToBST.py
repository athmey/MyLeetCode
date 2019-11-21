# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) is 0:
            return None

        else:
            mid = len(nums)//2
            treenode = TreeNode(nums[mid])
            nums1 = nums[0: mid]
            nums2 = nums[mid+1: len(nums)]
            treenode.left = self.sortedArrayToBST(nums1)
            treenode.right = self.sortedArrayToBST(nums2)

        return treenode