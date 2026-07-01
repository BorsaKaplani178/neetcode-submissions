class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_mapS = {}
        hash_mapT = {}

        for i in s:
            hash_mapS[i] = hash_mapS.get(i, 0) + 1
        
        for j in t:
            hash_mapT[j] = hash_mapT.get(j, 0) + 1
        
        if hash_mapS == hash_mapT:
            return True
        
        return False
        