class longestCommonPrefix(object):
    def myFirstSolution(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        pref = strs[0]

        i = 1

        while (i < len(strs)) and (pref != ""):
            while (pref != "") and not strs[i].startswith(pref):
                pref = pref[:-1]

            i += 1

        return pref

    def horizontal_scanning(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        pref = strs[0]

        for i in range(1, len(strs)):
            while (pref != "") and not strs[i].startswith(pref):
                pref = pref[:-1]

        return pref

    def my_vertical_scanning(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        i = len(strs)
        j = 0
        pref = -1

        while j < len(strs[0]) and i == len(strs):
            i = 0

            while i < len(strs) and len(strs[i]) > j:
                if strs[i][j] != strs[0][j]:
                    break
                i += 1

            if len(strs) == i:
                pref = j

            j += 1

        if pref > -1:
            return strs[0][:pref+1]

        return ""

    def vertical_scanning(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if (len(strs) == 0) or (strs is None):
            return ""

        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if (i == len(strs[j])) or (strs[j][i] != c):
                    return strs[0][:i]

        return strs[0]

     def longestCommonPrefix_strings(self, str_1, str_2):
        c = ""
        min_len = min(len(str_1), len(str_2))
        for i in range(min_len):
            if str_1[i] == str_2[i]:
                c+=str_1[i]
            else:
                return c
        return c
        
    def my_devide_conquer(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0 : 
            return ""
        elif len(strs) == 1: 
            return strs[0]
        elif len(strs)==2:
            return self.longestCommonPrefix_strings(strs[0], strs[1])
        else:
            mid = len(strs)/2
            print (mid)
            return self.longestCommonPrefix([self.longestCommonPrefix(strs[:mid]),\
                                            self.longestCommonPrefix(strs[mid:])])
    
    def dvide_conquer(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        return self.longestCommonPrefix_(strs, 0, len(strs)-1)
    
    def longestCommonPrefix_(self, strs, l, r):
        if l==r: return strs[l]
        else:
            mid = (l+r)/2
            lcpLeft = self.longestCommonPrefix_(strs, l, mid)
            lcpRight = self.longestCommonPrefix_(strs, mid+1, r)
            return self.commonPrefix(lcpRight, lcpLeft)
    
    def commonPrefix(self, left, right):
        min_len = min (len(left), len(right))
        for i in range(min_len):
            if right[i]!=left[i]:
                return left[:i]
        
        return left[:min_len]
