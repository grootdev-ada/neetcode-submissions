class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)        
        t1 = list(t)
        
        # Sort them first
        s1.sort()
        t1.sort()
        
        # Then compare them
        return s1 == t1
   
       
