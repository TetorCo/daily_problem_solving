class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_wealth = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > max_wealth:
                max_wealth = sum(accounts[i])
        return max_wealth