class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        for num in nums:
            if num in output:
                output[num] += 1
            else:
                output[num] = 1
        arr = []
        for num, count in output.items():
            arr.append([count, num])
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        return res