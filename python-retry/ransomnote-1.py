class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for i in ransomNote:
            if i in d:
                d[i] += d[i]+1
            else:
                d[i] = 1
        d1 = {}
        for i in magazine:
            if i in d1:
                d1[i] += d1[i]+1
            else:
                d1[i]=1
        
        
        for i in d:
            if i not in d1:
                return False
            if d[i]>d1[i]:
                return False
        return True
