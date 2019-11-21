# 706. 设计哈希映射

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__keys = []
        self.__vals = []

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        # 如果当前有这个key，则更新当前这个key对应的val值
        if self.__keys.count(key) == 1:
            index = self.__keys.index(key)
            self.__vals[index] = value

        # 如果没有这个key，则增加这对(key，val)
        else:
            self.__keys.append(key)
            self.__vals.append(value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if self.__keys.count(key) == 0:
            return -1
        else:
            return self.__vals[self.__keys.index(key)]

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if self.__keys.count(key) == 1:
            index = self.__keys.index(key)
            self.__vals.pop(index)
            self.__keys.remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)