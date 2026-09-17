class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mxs, cus = nums[0], 0
        for n in nums:
            if cus < 0:
                cus=0
            cus+=n
            mxs= max(mxs, cus)
        return mxs