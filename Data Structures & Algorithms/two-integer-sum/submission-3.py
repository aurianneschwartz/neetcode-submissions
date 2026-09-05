class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j:
                    continue
                if x+y == target:
                    return [i,j]
        """
        hashmap = {}

        for i in range(len(nums)):
            difference = target - nums[i] 
            if difference in hashmap:
                return [hashmap[difference],i]
            hashmap[nums[i]] = i
            

            