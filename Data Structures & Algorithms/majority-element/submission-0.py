class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        target = len(nums) // 2
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            if freq.get(n,0) > target:
                return n

            


        