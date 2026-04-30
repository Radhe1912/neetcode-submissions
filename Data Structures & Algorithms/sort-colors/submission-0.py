class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hm = {}

        for i in nums:
            hm[i] = hm.get(i, 0)+1

        count = 0
        for i in range(3):
            val = hm.get(i, 0)
            nums[count: count+val] = [i]*val
            count+=val
            
        return nums