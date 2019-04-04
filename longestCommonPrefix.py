class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) ==0 : return ""
        
        pref = strs[0]
        
        i = 1
        
        while (i < len(strs)) and (pref != ""):
            while (pref != "") and not strs[i].startswith(pref):
                pref = pref[:-1]
                
            i+=1
        
        return pref
