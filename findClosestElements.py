# 658. 找到 K 个最接近的元素
class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        res = []

        if arr is None or len(arr) == 0:
            return res

        if x < arr[0]:
            return arr[:k]

        elif x > arr[-1]:
            return arr[len(arr)-k:len(arr)]

        else:
            # 采用动态规划滑动窗的策略用一次遍历求得所需答案
            # 差值绝对值小的优先，元素小的优先
            diffs = []

            for num in arr:
                diffs.append(num-x)

            temp = diffs[0:k]
            # K个最接近的元素形成的距离和一定是最小的
            current_min_sum = sum([abs(val) for val in temp])
            global_min_sum = current_min_sum
            end = k-1

            for i in range(k, len(arr)):
                current_min_sum = current_min_sum - abs(diffs[i-k]) + abs(diffs[i])

                if current_min_sum < global_min_sum:
                    end = i
                    global_min_sum = current_min_sum

            res = arr[end+1-k:end+1]
            return res

