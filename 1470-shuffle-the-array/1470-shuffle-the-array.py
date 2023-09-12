class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        shuffle_list = []
        
        left_list = nums[:n]
        right_list = nums[n:]
        
        for idx in range(n):
            shuffle_list.append(left_list[idx])
            shuffle_list.append(right_list[idx])

        return shuffle_list