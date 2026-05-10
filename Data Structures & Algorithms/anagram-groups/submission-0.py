class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## brute force method:
        ## create an dictionary of dictionary
        ## Traverse through the list of inputs
        ## For each input, loop through the list of characters
            ## Compare it against a dictionary to see if all the letters can be found in the dictionary
                ## If yes, continue looping
                # If not, create a new dictionary to add the letter 

        ## Video explanation attempt
        
        
        dict = {}
        for i in strs:
            tuple_arr = ()
            arr = []
            for j in i:
                arr.append(j)
            arr.sort()
            tuple_arr = tuple(arr)
            if tuple_arr in dict:
                dict[tuple_arr].append(i)
            else:
                dict[tuple_arr] = [i]
        
        final_result = []
        for temp in dict:
            final_result.append(dict[temp]);
        return final_result