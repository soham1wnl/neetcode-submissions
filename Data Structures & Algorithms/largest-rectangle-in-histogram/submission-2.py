class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stax=[]
        mx=0

        for i,h in enumerate(heights):
            start=i
            while stax and h < stax[-1][1]:
                idx,ht=stax.pop()
                mx=max(mx,ht*(i-idx))
                start=idx
            stax.append([start,h])

        for i,h in stax:
            mx=max(mx,h*(len(heights)-i))

        return mx
                
        
            