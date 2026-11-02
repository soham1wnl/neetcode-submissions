class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stac=[]
        days=[0 for i in range(len(temperatures))]

        for i,t in enumerate(temperatures):
            while stac and t > stac[-1][1]:
                si,st=stac.pop()
                days[si]=i-si
            stac.append([i,t])

        return days
                