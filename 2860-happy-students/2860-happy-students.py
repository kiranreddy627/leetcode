class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        res=0
        n=len(nums)
        for i in range(1,n):
            if nums[i]>i and nums[i-1]<i:
                res+=1
        if 0 not in nums:
            res+=1
        if n>nums[-1]:
            res+=1
        return res