class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(typed) < len(name):
            return False

        list_name = list(name)
        list_typed = list(typed)

        # 利用滑动窗的思想去比对
        start = 0
        end = 0

        while end < len(list_name):
            # 说明是同一个字母，滑动窗继续增大
            if list_name[end] == list_name[start]:
                end += 1

            # 说明来到了另一个字母，滑动窗停止变化
            else:
                if len(list_typed) < end - start:
                    return False

                tmp = list_name[start:end]

                if tmp != list_typed[:end - start]:
                    return False

                else:
                    while len(list_typed) > 0 and list_typed[0] == list_name[start]:
                        list_typed.pop(0)

                    start = end

        # 做最后list_name剩余部分的处理
        if len(list_typed) < end - start:
            return False

        tmp = list_name[start:end]

        if tmp != list_typed[:end - start]:
            return False

        while len(list_typed) > 0:
            c = list_typed.pop(0)

            if c != list_name[start]:
                return False

        return True









