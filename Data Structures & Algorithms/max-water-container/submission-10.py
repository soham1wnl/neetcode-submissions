class Solution:
    def maxArea(self, h: List[int]) -> int:
        l,r=0,len(h)-1
        area,maxar=0,0

        while l<r:
            area=min(h[l],h[r])*(r-l)
            maxar=max(maxar,area)
            if h[l]<=h[r]: l+=1
            else: r-=1

        return maxar
