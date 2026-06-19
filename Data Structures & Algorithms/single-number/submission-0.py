class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rslt = 0

        for n in nums:
            rslt ^= n
        
        return rslt