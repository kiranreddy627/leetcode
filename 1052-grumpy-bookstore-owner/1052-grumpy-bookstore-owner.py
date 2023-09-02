class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans=0
        for i in range(len(customers)):
            if grumpy[i]==0:
                ans+=customers[i]
                customers[i]=0
        maxi=0
        curr=0
        for i,j in enumerate(customers):
            curr+=j
            if i>=minutes:
                curr-=customers[i-minutes]
            maxi=max(maxi,curr)
        return ans+maxi