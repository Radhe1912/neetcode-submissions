class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = [False]*len(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                used[i] = False

        backtrack([])
        return ans