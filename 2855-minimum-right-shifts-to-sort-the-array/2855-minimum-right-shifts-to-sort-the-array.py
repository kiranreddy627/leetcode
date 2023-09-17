class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        sor=sorted(nums)
        n=len(nums)
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:
                nums=nums[i:]+nums[:i]
                if nums==sor:
                    return n-i
                else:
                    return -1
        return 0
            