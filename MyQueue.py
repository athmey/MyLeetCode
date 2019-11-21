class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__myQueue = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.__myQueue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        last_element = self.__myQueue.pop(0)
        return last_element

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.__myQueue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.__myQueue) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()