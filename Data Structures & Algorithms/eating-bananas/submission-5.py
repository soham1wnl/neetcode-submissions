class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r,res=1,max(piles),max(piles)

        while l<=r:
            rate=(l+r)//2
            hr=0

            for p in piles:
                hr+=math.ceil(p/rate)
            
            if hr>h:
                l=rate+1
            else:
                res=min(res,rate)
                r=rate-1

        return res