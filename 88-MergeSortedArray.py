class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 1 and n == 0:
            return
        if m == 0 and n == 1:
            nums1[0] = nums2[0]
            return

        i, j, k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1            
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


        if i < 0:
            nums1[:k+1] = nums2[:j+1]

