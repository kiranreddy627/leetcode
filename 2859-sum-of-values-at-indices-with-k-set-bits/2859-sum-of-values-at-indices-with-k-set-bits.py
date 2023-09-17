class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ind=defaultdict(str)
        for i in range(len(nums)):
            ind[i]=bin(i)[2:]
        s=0
        for x,y in ind.items():
            if str(y).count("1")==k:
                s+=nums[x]
        return s