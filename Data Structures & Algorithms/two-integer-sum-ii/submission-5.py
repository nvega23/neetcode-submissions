class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if output[diff]:
                return [output[diff], i + 1]
            output[numbers[i]] = i + 1
        return []
