class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        s = 0

        for i in nums:
            if s<0:
                s = 0
            s+=i
            ans = max(ans, s)

        return ans