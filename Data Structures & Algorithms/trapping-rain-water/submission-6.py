class Solution:
    def trap(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        lm=heights[l];rm=heights[r]
        water=0

        while l<r:
            if lm<rm:
                l+=1
                lm=max(lm,heights[l])
                water+=lm-heights[l]
            else:
                r-=1
                rm=max(rm,heights[r])
                water+=rm-heights[r]

        return water
