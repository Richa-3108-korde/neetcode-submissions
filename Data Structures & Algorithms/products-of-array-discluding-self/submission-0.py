class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1 :
            return -1
    
        presum =[1]*len(nums)
        suffsum = [1]*len(nums)
        
        product1= 1

        for i  in range(1,len(nums)):

            product1 = product1* nums[i-1]
            presum[i] = product1
        
        product2 = 1 
        for i in range(len(nums)-2,-1,-1):
            product2 = product2 * nums[i+1]
            suffsum[i] = product2
        ans = [0]*len(nums)
        for i in range(len(nums)):

            ans[i] = presum[i] *suffsum[i]
        return ans 

            



        

        