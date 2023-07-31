class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst1=nums1+nums2
        lst1.sort()
        n=len(lst1)
        summ=0
        if n%2==0:
            summ=(lst1[n//2]+lst1[n//2-1])/2
        else:
            summ=lst1[(n)//2]
        return summ
