class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_idx in range(len(nums)):
            for second_idx in range(first_idx+1, len(nums)):
                if (nums[first_idx]+nums[second_idx]) == target:
                    return [first_idx, second_idx]