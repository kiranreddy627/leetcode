class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        vis=set()
        for i in nums:
            if i not in vis:
                vis.add(i)
            else:
                return i