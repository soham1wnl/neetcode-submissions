class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof,l,r=0,0,1

        while r<len(prices):
            if prices[r]>prices[l]: prof=max(prof,prices[r]-prices[l])
            else: l=r
            r+=1

        return prof