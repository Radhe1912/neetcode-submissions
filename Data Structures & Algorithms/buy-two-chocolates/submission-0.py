class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_one = float('inf')
        min_two = float('inf')

        for i in prices:
            if i<min_one:
                min_two = min_one
                min_one = i
            elif i<min_two:
                min_two = i

        ans = min_one+min_two
        return money-ans if money-ans>=0 else money