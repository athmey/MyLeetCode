class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        my_change = {5:0, 10:0, 20:0}

        for bill in bills:
            if bill == 5:
                my_change[5] += 1

            elif bill == 10:
                if my_change[5] >= 1:
                    my_change[5] -= 1
                    my_change[10] += 1
                else:
                    return False

            elif bill == 20:
                # 因为5块最灵活，所以优先用十块
                if my_change[10] >= 1:
                    if my_change[5] >= 1:
                        my_change[10] -= 1
                        my_change[5] -= 1

                        my_change[20] +=1
                    else:
                        return False

                elif my_change[10] < 1:
                    if my_change[5] >= 3:
                        my_change[5] -= 3
                        my_change[20] += 1

                    else:
                        return False
        return True