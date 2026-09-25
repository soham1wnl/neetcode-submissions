class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        resto= [1 for i in range(len(nums))]
        for i in range(1,len(nums)): resto[i]=resto[i-1]*nums[i-1]
        posto=1
        for i in range(len(nums)-1,-1,-1): resto[i]*=posto; posto*=nums[i]
        return resto