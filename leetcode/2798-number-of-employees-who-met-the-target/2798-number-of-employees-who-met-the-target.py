class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        result = 0

        for idx, value in enumerate(hours):
            if value >= target:
                result += 1

        return result