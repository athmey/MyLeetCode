# 784. 字母大小写全排列

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        result = []

        if S is None or len(S) == 0:
            return result

        tmp = ''
        self.permute(S, tmp, 0, result)

        return result

    def permute(self, S, tmp, start_index, result):
        # Return Condition
        if len(S) == len(tmp):
            result.append(tmp)

        else:
            # 如果当前位是数字
            if S[start_index].isdigit():
                tmp += S[start_index]

                self.permute(S, tmp, start_index+1, result)

            # 如果当前位是字母
            else:
                # 如果是大写字母
                if S[start_index].isupper():
                    tmp += S[start_index]
                    self.permute(S, tmp, start_index + 1, result)
                    tmp = tmp[:-1]

                    tmp += S[start_index].lower()
                    self.permute(S, tmp, start_index + 1, result)

                # 如果是小写字母
                else:
                    tmp += S[start_index]
                    self.permute(S, tmp, start_index + 1, result)
                    tmp = tmp[:-1]

                    tmp += S[start_index].upper()
                    self.permute(S, tmp, start_index + 1, result)

