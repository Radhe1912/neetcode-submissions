class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        count = 0
        
        while l<r:
            count = max(count, min(heights[l], heights[r])*(r-l))
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        

        return count