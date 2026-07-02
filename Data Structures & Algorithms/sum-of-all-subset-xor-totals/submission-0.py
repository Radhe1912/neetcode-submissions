class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        s = 0

        def f(al, xor, i):
            nonlocal s
            if i==len(nums):
                s+=xor
                return
            al.append(nums[i])
            f(al, xor^nums[i], i+1)
            al.pop()
            f(al, xor, i+1)

        f([], 0, 0)
        return s