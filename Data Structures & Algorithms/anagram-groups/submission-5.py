class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # establish a hash map
        output = {}
        # iterate over initial array
        for char in strs:
            # sort every word in the array
            sort = "".join(sorted(char))
            if sort in output:
                output[sort].append(char)
            else:
                output[sort] = [char]
        return list(output.values())
            # once sorted, group the words that have the same characters
        # return sort
        # return the values from the hashmap
