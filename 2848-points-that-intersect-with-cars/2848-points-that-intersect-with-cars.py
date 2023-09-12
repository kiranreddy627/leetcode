class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        lst=[]
        for i,j in nums:
            lst.extend(list(range(i,j+1)))
        vis=set(lst)
        return len(vis)