class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for num in nums:
            output[num] = output.get(num, 0) + 1
        return sorted(output, key=output.get, reverse=True)[:k]
