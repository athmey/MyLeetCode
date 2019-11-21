class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__minStack = list()
        self.__stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.__stack.append(x)

        if len(self.__minStack) == 0 or x <= self.__minStack[-1]:
            self.__minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.__stack) >= 1:
            elem = self.__stack.pop(-1)

            if elem == self.__minStack[-1]:
                self.__minStack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        if len(self.__minStack) >= 1:
            return self.__stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()