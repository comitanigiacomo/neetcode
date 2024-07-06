from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # se la chiave non esiste ancora nella mappa, la funzione ritorna 0, e in questo caso viene quindi assegnato 1 come valore
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS: 
            if countS[c] != countT.get(c, 0): return False # Anche qui nel caso in cui in t non ci sia una lettera presente in a, per evitare keyerror la funzione mette 0 come valore
        
        return True
        
        
s = "racecar"
t = "carrace"
sol = Solution()
print(sol.isAnagram(s, t))