class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       viewed = {}
       for i, num in enumerate(nums):
            if target - num in viewed:
                return [viewed[target-num],i]
            viewed[num] = i