class Solution(object):
    def merge(self, nums1, m, nums2, n):
       for i in range(n):
        nums1[m+i] = nums2[i]
       total = m+n
       for i in range(total):
        for j in range(i+1 , total):
            if nums1[i] > nums1[j]:
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp
       return nums1
         