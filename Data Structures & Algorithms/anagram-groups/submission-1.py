class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## traverse through the list of strs
        ## create an array with 26 0's to represent each alphabet
        ## For each character in strs, find the ascii form of it, 
        ## Subtract it by the ascii of 'a' to find its relative index 
        ## to a, ie. a = 10, b = 11, 11-10 = 1, the index of b in the array
        ## use this array (convert to truple) as the key of the dictionary, 
        ## mapping to an array of strs
        ## Return all the values of dictionary

        result = defaultdict(list)
        for s in strs:
            temp = [0] * 26
            for char in s:
                temp[ord(char)-ord('a')] += 1

        
            result[tuple(temp)].append(s)
            

        
        return list(result.values())
