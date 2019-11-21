# 705. 设计哈希集合

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__set = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.__set.count(key) == 0:
            self.__set.append(key)
        else:
            pass

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if self.__set.count(key) > 0:
            self.__set.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.__set.count(key) > 0

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)