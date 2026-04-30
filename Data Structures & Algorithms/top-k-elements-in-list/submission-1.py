class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        hq = []

        for num, count in freq.items():
            heapq.heappush(hq, (count, num))
            if len(hq)>k:
                heapq.heappop(hq)

        res = []

        while hq:
            res.append(heapq.heappop(hq)[1])

        return res
        
        # d = {}

        # for i in nums:
        #     d[i] = d.get(i, 0)+1

        # hm = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

        # return list(hm.keys())[:k]