class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # res={}
        # ans=[]
        # for i in range(len(dist)):
        #     a=dist[i]
        #     temp=[]
        #     for j in dist:
        #         temp.append(j/a)
        #     res[i].append(sum(temp))
        # for i in range(len(res)):
        #     if res[i]<=hour:
        #         ans.append(i)
        # return min(ans)
        def fun(dist,mid):
            s=0
            for i in dist:
                s=ceil(s)
                speed=i/mid
                s+=speed
            return s<=hour
        l=1
        r=10**7
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if fun(dist,mid):
                r=mid-1
                ans=mid
            else:
                l=mid+1
        return ans