import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = Counter(nums)
        return heapq.nlargest(k, output.keys(), output.get)

