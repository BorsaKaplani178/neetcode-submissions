class Solution:
    def firstUniqChar(self, s: str) -> int:
        result = defaultdict(int)

        for c in s:
            result[c] += 1
        
        for i, c in enumerate(s):
            if result[c] == 1:
                return i
        
        return -1
        