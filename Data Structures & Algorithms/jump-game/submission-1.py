class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpRange = nums[0]

        for i in range(1, len(nums)):
            if jumpRange <= 0:
                return False
            jumpRange -= 1

            jumpRange = max(jumpRange, nums[i])

        return True