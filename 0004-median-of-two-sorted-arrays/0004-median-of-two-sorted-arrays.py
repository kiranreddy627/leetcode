class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst1=nums1+nums2
        lst1.sort()
        n=len(lst1)
        s=0
        if n%2==0:
            s=(lst1[n//2]+lst1[n//2-1])/2
        else:
            s=lst1[(n)//2]
        return s