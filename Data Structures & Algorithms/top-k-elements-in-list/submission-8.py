import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use a hash map to count how many times a number is repeated
        # return the most counted number that was repeated
        # use a counter and use it against the value in the hash map
        output = Counter(nums)
        return heapq.nlargest(k, output.keys(), output.get)
