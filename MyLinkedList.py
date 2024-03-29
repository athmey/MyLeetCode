class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__myLinkedList = list()


    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        # print(self.__myLinkedList)
        # print('list length: ', len(self.__myLinkedList))
        # print('Index', index)
        if index >= len(self.__myLinkedList):
            return -1
        else:
            return self.__myLinkedList[index]

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.__myLinkedList.insert(0, val)
        # print(self.__myLinkedList)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.__myLinkedList.append(val)
        # print(self.__myLinkedList)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > len(self.__myLinkedList):
            return
        self.__myLinkedList.insert(index, val)
        # print(self.__myLinkedList)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index >= len(self.__myLinkedList):
            return
        self.__myLinkedList.pop(index)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)