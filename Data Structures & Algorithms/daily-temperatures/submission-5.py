class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack=[]
        res= [0 for i in range(len(temps))]

        for i,t in enumerate(temps):
            while stack and t > stack[-1][1]:
                si,st=stack.pop()
                res[si]=i-si
            stack.append([i,t])

        return res

        
        