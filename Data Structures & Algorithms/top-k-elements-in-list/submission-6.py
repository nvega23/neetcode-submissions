import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a heap
        # heap.nlargest(num)
        # return heap[:k]
        freq_map = Counter(nums)
        return heapq.nlargest(k, freq_map.keys(), key=freq_map.get)
