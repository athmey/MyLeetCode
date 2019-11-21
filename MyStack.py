class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__stack = list()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.__stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        top_element = self.__stack.pop()
        return top_element

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.__stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.__stack) is 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()