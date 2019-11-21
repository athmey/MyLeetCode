class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        # 811. 子域名访问计数
        if cpdomains is None or len(cpdomains) == 0:
            return []

        res = []
        records = {}

        # ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
        for domain in cpdomains:
            time = int(domain.split()[0])

            domain_name = domain.split()[1]

            # names中存储着当前domain_name所能形成的所有域名
            names = self.generateName(domain_name)

            for name in names:
                if name not in records.keys():
                    records[name] = time
                else:
                    records[name] += time

        for key in records.keys():
            buff = ''

            buff += str(records[key]) + ' ' + str(key)

            res.append(buff)

        return res

    def generateName(self, domain_name):
        if domain_name is None or len(domain_name) == 0:
            return []

        domain_name = domain_name.strip()

        res = []

        subnames = domain_name.split('.')

        tmp = ''
        for i in range(len(subnames)-1, -1, -1):
            if tmp == '':
                tmp = subnames[i] + tmp
            else:
                tmp = subnames[i] + '.' + tmp

            res.append(tmp)

        return res


