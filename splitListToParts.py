# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # 计算链表的长度
        length = 0
        cur = root

        while cur is not None:
            length +=1
            cur = cur.next

        group_min_length = length // k
        print("group_min_length: ",group_min_length)

        if group_min_length < 0:
            return [root]

        num_of_min_length_group = (group_min_length+1)*k-length
        num_of_max_length_group = k - num_of_min_length_group

        print("Min num: ", num_of_min_length_group)
        print("Max num: ", num_of_max_length_group)

        result = list()
        cur = root
        result.append(cur)

        # 找到每个链表的起点和终点
        # 先长链表
        for i in range(num_of_max_length_group):
            for j in range(max(0, group_min_length + 1 - 1)):
                print("Root: ", cur is root)
                if cur is root:
                    pass
                cur = cur.next

            print("Loop1: ", cur.val)
            if cur is not None:
                tmp = cur
                cur = cur.next
                tmp.next = None
            result.append(cur)

        if len(result) == k:
            return result

        # 短链表
        for i in range(num_of_min_length_group):
            for j in range(max(0, group_min_length - 1)):
                if cur is root:
                    pass
                cur = cur.next

            print("Loop2")
            if cur is not None:
                tmp = cur
                cur = cur.next
                tmp.next = None
            result.append(cur)

        if len(result) != k:
            result.pop()

        return result
