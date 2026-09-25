class Solution:

    def encode(self, strs: List[str]) -> str:
    
        result = ""

        for word in strs:
            result += str(len(word)) + "#" + word

        return result
 


    def decode(self, s: str) -> List[str]:
        result = []
        position = 0

        while position < len(s):
            hash_position = position

            while s[hash_position] != "#":
                hash_position +=1
            
            length = int(s[position:hash_position])

            word_start = hash_position + 1

            word = s[word_start:word_start + length]

            result.append(word)
            
            position = word_start + length
        return result



        
