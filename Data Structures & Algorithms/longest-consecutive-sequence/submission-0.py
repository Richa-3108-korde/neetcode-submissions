class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hash_set = set(nums)
        max_length = 0
        for i in hash_set:

            if i -1 in hash_set:
                continue 
            count = 1 
            while i+1 in hash_set:
                
                count = count + 1 
                i = i + 1 
            max_length = max(max_length,count)
        return max_length 


        