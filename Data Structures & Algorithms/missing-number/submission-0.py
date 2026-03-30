class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = (len(nums)+1)*len(nums)/2

        return int(total - sum(nums))
