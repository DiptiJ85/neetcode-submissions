class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = 0
        right = len(s)
        isAna = True
        result = {}
        if len(s)!=len(t):
            isAna = False
        else:
            for ss in s:
                if ss not in result:
                    result[ss] = 1
                else:
                    result[ss]+= 1
            for tt in t:
                if tt not in result:
                    isAna = False
                    break
                else:
                    result[tt]-=1
                    if result[tt]==0:
                        del result[tt]
            if len(result)!=0:
                isAna = False
        return isAna

                    
