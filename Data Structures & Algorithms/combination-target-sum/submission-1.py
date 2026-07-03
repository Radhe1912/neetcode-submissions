class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        def rec(al, i, s):
            if s==target:
                ans.append(al[:])
                return
            if i>=n:
                return
            if nums[i]<=target-s:
                al.append(nums[i])
                rec(al, i, s+nums[i])
                al.pop()
            
            rec(al, i+1, s)

        rec([], 0, 0)
        return ans