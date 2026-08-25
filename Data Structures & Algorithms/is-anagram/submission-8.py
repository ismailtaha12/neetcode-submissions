class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)
        for char_s , char_t in zip(s,t):
            count[char_s] += 1
            count[char_t] -= 1

        for val in count.values():
            if val != 0:
                return False
        
        return True