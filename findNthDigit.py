
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        个位数：1-9，一共9个,共计9个数字
        2位数：10-99,一共90个，共计180个数字
        3位数：100-999，一共900个，共计270个数字
        4位数，1000-9999，一共9000个，共计36000个数字  36000=4*9*10**（4-1）
        ......
        """
        #第一步确定n是在几位数里，第二步是确定在几位数的第几位数字的第几位
        #第一步
        digit=1#位数
        while n>digit*9*10**(digit-1):
            n-=digit*9*10**(digit-1)
            digit+=1

        #第二步
        a=int((n-1)/digit)#得到几位数的第几位数字
        b=int((n-1)%digit)#得到几位数的第几位数字的第几位
        num=10**(digit-1)+a#得到第几位数字是多少
        res=list(str(num))[b:b+1]#数字转字符再转列表把第几位数的第几位切出来
        return int(''.join(res))#列表转字符再转数字
