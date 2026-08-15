class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nestList = {}
        for word in strs:
            s1 = tuple(sorted(word))
            if s1 not in nestList:
                nestList[s1]=[]
            nestList[s1].append(word)
           # print (s1)   
        return list(nestList.values())

        
        