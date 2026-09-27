class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for a in range(len(nums) - 2):
            if nums[a] > 0:
                break

            left = a + 1
            right = len(nums) - 1

            while left < right:
                total = nums[a] + nums[left] + nums[right]

                if total == 0:
                    result.add((nums[a], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1

        return [list(triplet) for triplet in result]