class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        idx_list = []

        for idx in range(len(address)):
            if address[idx] == '.':
                idx_list.append(idx)

        for idx, value in enumerate(idx_list):
            insert_value = (idx * 2) + value
            address = address[:insert_value] + '[' + address[insert_value:insert_value+1] + ']' + address[insert_value+1:]

        # address = ''.join([char.replace(".", "[.]") for char in address])
        ## replace를 이용해서 문자열을 치환해주는 방법이 더 간단.
        return address