class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        nums[n-1] = 0
        
        for i in range(n-2, -1, -1):
            minJump = math.inf
            for j in range(i+1, min(n, i+nums[i]+1)):
                minJump = min(minJump, nums[j])
            nums[i] = minJump + 1
        
        return nums[0]