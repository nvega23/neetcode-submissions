class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = defaultdict(int)
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in output:
                return [output[diff], i+1]
            output[numbers[i]] = i + 1
        return []
        