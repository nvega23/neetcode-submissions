class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}

        for word in strs:
            joined = "".join(sorted(word))
            if joined in output:
                output[joined].append(word)
            else:
                output[joined] = [word]
        return list(output.values())

