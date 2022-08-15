class Solution(object):
    def romanToInt(self, string):
        """
        :type s: str
        :rtype: int
        """
        convertInt, i = 0, 0
        romanNumberDict = {'I' : 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
                            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        while i < len(string):
            try:
                convertInt += romanNumberDict[string[i]+string[i+1]]
                i += 2
            except:
                convertInt += romanNumberDict[string[i]]
                i += 1

        return convertInt