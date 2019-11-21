class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        if emails is None and len(emails) is 0:
            return 0

        result = set()

        for email in emails:
            if email.find('@') == -1:
                continue

            segments = email.split('@')
            local_name = segments[0]
            dominant_name = segments[1]

            # Deal with the local_name issue:
            first_plus_symbol_pos = 0

            for i in range(len(local_name)):
                if local_name[i] is '+':
                    first_plus_symbol_pos = i
                    break
            if i is 0:
                continue
            else:
                local_name = local_name[:first_plus_symbol_pos]
                local_name_revised = ''

                for c in local_name:
                    if c is not '.':
                        local_name_revised = local_name_revised + c

                whole_name = ''
                if len(local_name_revised.strip()) is not 0:
                    whole_name = whole_name + local_name_revised + '@' + dominant_name

                result.add(whole_name)

        return len(result)