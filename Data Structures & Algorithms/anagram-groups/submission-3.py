class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for char in strs:
            sort = "".join(sorted(char))
            if sort in res:
                res[sort].append(char)
            else:
                res[sort] = [char]
        return list(res.values())