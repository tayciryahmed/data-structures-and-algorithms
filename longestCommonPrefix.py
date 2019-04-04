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
