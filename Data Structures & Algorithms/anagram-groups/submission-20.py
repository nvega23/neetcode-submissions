class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for words in strs:
            sortS = "".join(sorted(words))
            if sortS in output:
                output[sortS].append(words)
            else:
                output[sortS] = [words]
        return list(output.values())

