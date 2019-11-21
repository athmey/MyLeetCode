# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head is None:
            return None

        vals = list()

        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next

        return self.sortedArrayToBST(vals)

    def sortedArrayToBST(self, nums):
        if nums is None or len(nums) is 0:
            return None

        else:
            mid = len(nums)//2
            treenode = TreeNode(nums[mid])

            treenode.left = self.sortedArrayToBST(nums[0:mid])
            treenode.right = self.sortedArrayToBST(nums[mid+1:])

            return treenode
