class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = {}

        for i in range(len(nums)):
            if target - nums[i] in hash:
                ind = hash[target-nums[i]]

                return [min(ind,i),max(ind,i)]
            else :
                hash[nums[i]] = i 
        return -1
            

        
            

                
        