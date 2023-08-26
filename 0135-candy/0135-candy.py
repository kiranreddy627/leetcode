class Solution:
    def candy(self, ratings: List[int]) -> int:
        l1=[1]*len(ratings)
        l2=[1]*len(ratings)
        res=0
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                l1[i]=l1[i-1]+1
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                l2[i]=l2[i+1]+1
        
        for i in range(len(ratings)):
            res+=max(l1[i],l2[i])
        return res