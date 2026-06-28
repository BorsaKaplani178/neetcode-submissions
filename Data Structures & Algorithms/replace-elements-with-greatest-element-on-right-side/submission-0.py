class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []

        for i in range(len(arr)):
            rightMax = -1
            for j in range(i + 1, len(arr)):
                rightMax = max(rightMax, arr[j])
            result.append(rightMax)
        return result