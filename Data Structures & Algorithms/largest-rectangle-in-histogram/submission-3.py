class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        mx=0

        for i,h in enumerate(heights):
            start=i
            while stack and h < stack[-1][1]:
                idx,ht=stack.pop()
                mx=max(mx,ht*(i-idx))
                start=idx
            stack.append([start,h])

        for i,h in stack:
            mx=max(mx,h*(len(heights)-i))

        return mx