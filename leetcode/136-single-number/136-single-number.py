class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = collections.Counter(nums)
        for key, value in result.items():
            if value == 1:
                return key