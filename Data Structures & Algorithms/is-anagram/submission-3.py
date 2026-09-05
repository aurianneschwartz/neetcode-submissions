from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = defaultdict(int)
        for char in s:
                hm[char] += 1
        
        for char in t:
            if char not in hm:
                return False
            else:
                hm[char] -= 1
                if hm[char] < 0:
                    return False
        
        if sum(hm.values()) == 0:
            return True

        return False