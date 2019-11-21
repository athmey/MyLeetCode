class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = list()
        for i in range(1,n+1):
            if i % 3 is not 0 and i % 5 is not 0:
                result.append(str(i))

            elif i % 3 is 0 and i % 5 is not 0:
                result.append('Fizz')

            elif i % 3 is not 0 and i % 5 is 0:
                result.append('Buzz')

            else:
                result.append('FizzBuzz')

        return result
