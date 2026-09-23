class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset = set(nums)
        if myset == nums:
            return False
        return True        