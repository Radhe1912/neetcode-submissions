class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = nums[:]
        heapq.heapify(heap)
        arr = []

        while heap:
            arr.append(heapq.heappop(heap))

        return arr
        
        # heap = []
        # for i in nums:
        #     heapq.heappush(heap, i)

        # arr = []
        # while heap:
        #     arr.append(heapq.heappop(heap))
        # return arr