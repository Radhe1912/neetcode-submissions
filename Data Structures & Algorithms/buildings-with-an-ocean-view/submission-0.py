class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        val = 0

        for i in range(len(heights)-1, -1, -1):
            if heights[i]>val:
                ans.append(i)
            val = max(val, heights[i])

        return ans[::-1]