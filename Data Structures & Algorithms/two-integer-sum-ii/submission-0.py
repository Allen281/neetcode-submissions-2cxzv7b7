class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        curSum = numbers[left] + numbers[right]
        while curSum != target:
            if curSum < target:
                left += 1
            else: right -= 1

            curSum = numbers[left] + numbers[right]
        
        return [left+1, right+1]


