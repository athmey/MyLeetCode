class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # 443.压缩字符串
        if len(chars) == 1:
            return 1

        start = 0
        end = 0
        counter = 0

        index = 0

        while end < len(chars):
            # 当前同一个字母，统计该字母的个数
            if chars[end] == chars[start]:
                counter += 1
                end += 1

            # 遇到了不同的字母，开始统计上一个字母的信息
            else:
                # 先将字母替换
                char = chars[start]
                chars[index] = char
                index += 1

                # 再将数量写进原数组
                if counter > 1:
                    for c in str(counter):
                        chars[index] = c
                        index += 1

                counter = 0
                start = end

        # 收尾工作，防止漏处理
        # 先将字母替换
        char = chars[start]
        chars[index] = char
        index += 1

        # 再将数量写进原数组
        if counter > 1:
            for c in str(counter):
                chars[index] = c
                index += 1

        return index