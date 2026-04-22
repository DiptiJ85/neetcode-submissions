class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c.lower())-ord("a")]+=1
        #if str(count)  not in res:
         #   res[str(count)] = list()
            res[str(count)].append(s)
        return list(res.values())
        
        