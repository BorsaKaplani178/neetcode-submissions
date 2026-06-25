class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        array = []
        result = []

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        for key, value in hash_map.items():
            array.append([value, key])
        array.sort()

        while len(result) < k:
            result.append(array.pop()[1])
        return result




