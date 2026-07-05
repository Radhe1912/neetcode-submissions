class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        read = 0
        write = 0

        if n<=2:
            return n

        while read<n:
            curr = nums[read]
            val = 0
            while read<n and curr==nums[read]:
                read+=1
                val+=1
            if val>1:
                nums[write] = curr
                nums[write+1] = curr
                write+=2
            else:
                nums[write] = curr
                write+=1
            
        return write