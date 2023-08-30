class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res=0
        curr=capacity
        for i,j in enumerate(plants):
            if curr<j:
                res+=2*i
                curr=capacity
            res+=1
            curr-=j
        return res
