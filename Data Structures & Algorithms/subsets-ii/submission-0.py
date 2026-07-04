class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        nums.sort()

        def backTrack(al, i):
            if i==n:
                arr.append(al[:])
                return
            
            al.append(nums[i])
            backTrack(al, i+1)
            al.pop()
            
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            backTrack(al, i+1)

        backTrack([], 0)
        return arr