class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        
        for x in strs:
            arr = [0]* 26
            for l in x :
                arr[ord(l)-ord('a')] += 1
                   
            res[tuple(arr)].append(x)
        return res.values()
                
                   