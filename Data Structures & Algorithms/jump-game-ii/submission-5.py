class Solution:
    def jump(self, nums: List[int]) -> int:
    
        max_jump = 0
        min_num_jump = 0
        last_max_reachable = 0

        for i, num in enumerate(nums):
            
            cur_jump = i + num
            max_jump = max(max_jump, cur_jump)
            
            if last_max_reachable <= i and i != len(nums)-1:
                min_num_jump +=1
                last_max_reachable = max_jump

                if last_max_reachable >= len(nums)-1:
                    break

        
        return min_num_jump