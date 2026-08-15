class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check: if lengths are different, it's impossible
        if len(s) != len(t):
            return False
            
        # Create an empty dictionary to hold our letter counts
        counts = {}
        
        # Loop through both strings at the same time
        for i in range(len(s)):
            # Add 1 for letters in 's'
            counts[s[i]] = counts.get(s[i], 0) + 1
            # Subtract 1 for letters in 't'
            counts[t[i]] = counts.get(t[i], 0) - 1
            
        # If they are perfect anagrams, every count should have zeroed out
        for count in counts.values():
            if count != 0:
                return False
                
        return True