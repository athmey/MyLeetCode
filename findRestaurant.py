class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        result = list()
        if list1 is None or list2 is None:
            return result

        if len(list1) is 0 or len(list2) is 0:
            return result

        names_in_common = list()
        for name in list1:
            if name in list2:
                names_in_common.append(name)

        records = dict()
        copy = list1+list2

        for index,val in enumerate(copy):
            if val in names_in_common:
                if val not in records.keys():
                    records[val] = index
                else:
                    records[val] += index

        sorted_records = sorted(records.items(), key = lambda x:x[1])
        result = list()
        min = sorted_records[0][1]
        for pair in sorted_records:
            if pair[1] == min:
                result.append(pair[0])
        return result
