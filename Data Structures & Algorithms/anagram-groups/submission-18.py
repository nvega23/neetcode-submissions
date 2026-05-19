class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash map {}
        # array [] 
        # iterate over the array
        # sort the words = car = acr.
        # If we have two "car" or acr [acr, acr]
        # if the sorted word is in the hashmap, append the char to the array
        # if not, add it to the hashmap
        # return the hashmaps values 
        output = {}
        for char in strs:
            sort = "".join(sorted(char))
            if sort in output:
                output[sort].append(char)
            else:
                output[sort] = [char]
        return list(output.values())
