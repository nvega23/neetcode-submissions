class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for char in strs:
            joined = ''.join(sorted(char))
            if joined in output:
                output[joined].append(char)
            else:
                output[joined] = [char]
        return output.values()

