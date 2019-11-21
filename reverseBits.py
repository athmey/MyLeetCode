class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n_bin = bin(n)[2:]
        print(n_bin)

        print(len(n_bin))

        while len(n_bin) < 32:
            n_bin = '0' + n_bin

        print(n_bin)

        reverse = str(n_bin)[::-1]

        return int(reverse, 2)
