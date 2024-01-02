class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        charsS1 = [0]* 26
        for i in range(len(s1)):
            charsS1[ord(s1[i]) - ord("a")] += 1 

        charsS = [0]* 26
        for i in range(len(s1)-1):
            charsS[ord(s2[i]) - ord("a")] += 1 
        
        l=0
        for r in range(len(s1)-1, len(s2)):
            charsS[ord(s2[r]) - ord("a")] += 1 
            isPermut = True
            for i in range(26):
                if charsS[i] != charsS1[i]:
                    isPermut = False
                    charsS[ord(s2[l]) - ord("a")] -= 1 
                    l += 1
                    break
            if isPermut:
                return True
        
        return False
            

                


