class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            n = nums[i]
            if n in seen:
                return True
            seen.add(n)
        return False
