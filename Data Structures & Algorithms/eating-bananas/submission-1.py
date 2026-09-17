class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r,res=1,max(piles),max(piles)

        while l<=r:
            k=(r+l)//2
            hrs=0
            for p in piles:
                hrs+=math.ceil(p/k)
            
            if hrs<=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1

        return res
        