class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_array = []
        i,j = 0, 0
        len1, len2 = len(nums1), len(nums2)
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                merge_array.append(nums1[i])
                i+=1

            else:
                merge_array.append(nums2[j])
                j+=1

        while i < len1:
            merge_array.append(nums1[i])
            i+=1

        while j < len2:
            merge_array.append(nums2[j])
            j+=1

        mid = (len1+len2)//2
        if (len1+len2)%2 != 0:
            return merge_array[mid]
        return (merge_array[mid] + merge_array[mid-1])/2
    
#Memory: O(m+n)
#Time: O(log(m+n))