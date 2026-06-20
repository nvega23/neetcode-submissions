class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for char in strs:
            fixed = "".join(sorted(char))
            if fixed in output:
                output[fixed].append(char)
            else:
                output[fixed] = [char]
        return list(output.values())