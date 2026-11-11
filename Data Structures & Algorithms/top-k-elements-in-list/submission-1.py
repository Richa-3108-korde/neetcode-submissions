class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        repeating = {}

        for i in nums:
            if i not in repeating  :
                repeating[i] = 1 
            else :
                repeating[i] += 1
        ans =[]
        sorted_dict = dict(sorted(repeating.items(), key=lambda x: x[1], reverse=True))
        for keys in sorted_dict:

            if k == 0 :
                return ans
            else:
                ans.append(keys)
                k = k-1 
        return ans 




        