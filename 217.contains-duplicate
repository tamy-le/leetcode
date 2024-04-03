class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #return len(nums) > len(set(nums)) #Easy solution
        #Optimize (can return immediately if self implemented)
        hash_dict = {}
        for i in range(len(nums)):
            if nums[i] not in hash_dict:
                hash_dict[nums[i]]=1
            else:
                return True
        return False

#Time: O(n)
#Memory: O(n)