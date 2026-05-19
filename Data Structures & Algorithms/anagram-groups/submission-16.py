class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for char in strs:
            sChar = ''.join(sorted(char))
            if sChar in output:
                output[sChar].append(char)
            else:
                output[sChar] = [char]
        return list(output.values())