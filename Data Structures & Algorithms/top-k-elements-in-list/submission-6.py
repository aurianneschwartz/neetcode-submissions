from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:     
        
        douglas = defaultdict(int)
        result = []

        for num in nums:
            douglas[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in douglas.items():
            buckets[value].append(key)

        for bucket in buckets[::-1]:
            for num in bucket:
                if len(result) < k:
                    result.append(num)

        return result