class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort the characters in the array
        # append the char if they have been seen in a hash map
        # return the new hash map
        output = {}
        for char in strs:
            sort = ''.join(sorted(char))
            if sort in output:
                output[sort].append(char)
            else:
                output[sort] = [char]
        return list(output.values())