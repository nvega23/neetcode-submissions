class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for char in strs:
            sort = ''.join(sorted(char))
            if sort in output:
                output[sort].append(char)
            else:
                output[sort] = [char]
        return output.values()
        