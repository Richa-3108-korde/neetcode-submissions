class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hash = []
        n = len(nums)
        for i in range(n):

            if nums[i] in hash:
                return True
            hash.append(nums[i])
        return False 
        

        
 