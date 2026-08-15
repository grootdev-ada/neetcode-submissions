class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nestList = {}
        
        for word in strs:
            # 1. Create an array of 26 zeros
            count = [0] * 26 
            
            # 2. Count the letters in the word
            for char in word:
                # This turns 'a' into 0, 'b' into 1, 'c' into 2, etc.
                index = ord(char) - ord('a') 
                count[index] += 1
                
            # 3. Lock the count array into a tuple to use as our signature
            signature = tuple(count)
            
            # 4. Same dictionary logic as before!
            if signature not in nestList:
                nestList[signature] = []
            nestList[signature].append(word)
            
        return list(nestList.values())