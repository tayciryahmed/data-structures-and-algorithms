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
