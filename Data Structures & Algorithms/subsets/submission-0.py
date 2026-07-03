class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        arr = []
        
        def rec(al, i):
            if i==n:
                arr.append(al[:])
                return
            al.append(nums[i])
            rec(al, i+1)
            al.pop()
            rec(al, i+1)

        rec([], 0)
        return arr