class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        for word in strs:
            sortWord = ''.join(sorted(word))
            if sortWord in output:
                output[sortWord].append(word)
            else:
                output[sortWord] = [word]
        return list(output.values())