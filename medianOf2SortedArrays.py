'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
            
        
        #if len(nums1)==0 or len(nums2) and len(nums1)!=len(nums2):       
        n=(len(nums1)+len(nums2))/2 
        j=0
        k=0
        a=[]
        
        median=0
        while j<len(nums1) and k<len(nums2):
            
            if nums1[j]<nums2[k]:
                a.append((nums1[j]))
                j+=1
            else:
                a.append((nums2[k]))
                k+=1
        if j==len(nums1):
            a.extend(nums2[k:])
        if k==len(nums2):
            a.extend(nums1[j:])
        
        if (len(nums1)+len(nums2))%2==0:
            median=float((a[int(n)]+a[int(n-1)])/2)    
        else:
            
            median=float(a[int(n)])
        return median