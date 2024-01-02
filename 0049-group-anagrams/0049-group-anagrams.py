class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for idx in set(s):
                if s.count(idx) != t.count(idx):
                    return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for s in strs : 
            myMap[''.join(sorted(s))].append(s)
        
        return list(myMap.values())