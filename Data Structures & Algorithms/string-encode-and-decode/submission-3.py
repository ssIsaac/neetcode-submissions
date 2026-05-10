class Solution:

    # ["Hello", "World"] -> "Hello#World"
    # Can use a separator like '#'. However, if the content of the vector contains a '#', it would not be valid
    # Use a dictionary to keep track of the index?

    # ["Hello#", "#World"]
    #"Hello##0#World#1"
    #["Hello"]

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        encode_arr = ""
        index = ""
        for i in range(len(strs)):
            encode_arr += strs[i]
            index += str(len(strs[i])) + "#"
        encode_arr += index + str(len(index)-1)
        return encode_arr
    # "HelloWorld5#5#3"
    # ["HelloWorld]

    # "Hello#World" -> ["Hello", "World"]
    def decode(self, s: str) -> List[str]:
        if(s == ""):
            return []
        decode_arr = []
        index_length = s.split("#")[-1] #"3"
        starting_index = len(s)- len(index_length) - 1 - int(index_length) #10
        index = s[starting_index:starting_index+int(index_length)].split("#") #["5", "5"]
        print(s)
        counter = 0
        for i in index:
            decode_arr.append(s[counter:counter+int(i)])
            counter += int(i)

        return decode_arr