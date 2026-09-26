class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = nums[:k]
        seen = set(window)
        l = 0
        
        if len(seen) < len(window):
            return True
        
        for r in range(k, len(nums)):

            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            seen.remove(nums[l])
            l +=1
        return False
        