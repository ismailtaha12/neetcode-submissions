class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqmap = {}
        for i  in range(len(nums)):
            n = nums[i]
            freqmap[n] = freqmap.get(n,0) + 1
            if freqmap.get(n , 0) > 1:
                return True
        
            
        return False            