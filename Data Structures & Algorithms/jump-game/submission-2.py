class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_jump = 0

        for idx, num in enumerate(nums):

            if idx > max_jump:
                return False

            cur = idx + num
            if cur > max_jump :
                max_jump = cur

            if max_jump >= len(nums) - 1:
                return True


        return False