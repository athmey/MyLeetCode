# 933. 最近的请求次数

class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        # 将小于当前t-3000的时间全部弹出队列
        while (len(self.queue) > 0) and (self.queue[0] < t - 3000):
            self.queue.pop(0)

        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)