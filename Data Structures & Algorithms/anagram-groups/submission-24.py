class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for char in strs:
            sorts = ''.join(sorted(char))
            if sorts in output:
                output[sorts].append(char)
            else:
                output[sorts] = [char]

        return list(output.values())

