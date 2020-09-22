class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        n2w = {1e9: "Billion", 1e6: "Million", 1e3: "Thousand", 1e2: "Hundred",
               90:  "Ninety", 80:  "Eighty", 70:  "Seventy",
               60:  "Sixty", 50:  "Fifty", 40:  "Forty",
               30:  "Thirty", 20:  "Twenty", 19: "Nineteen",
               18:  "Eighteen", 17: "Seventeen", 16: "Sixteen",
               15:  "Fifteen", 14: "Fourteen", 13: "Thirteen",
               12:  "Twelve", 11:  "Eleven", 10:  "Ten",
               9:   "Nine", 8:   "Eight", 7:   "Seven",
               6:   "Six", 5:   "Five", 4: "Four", 3: "Three",
               2: "Two", 1: "One", 0: "Zero"}


        def dp(n):
            if n <= 20: return n2w[n]
            for div in n2w.keys():
                d, r = divmod(n, div)
                if not d: continue
                s1 = dp(d) + " " if div >= 100 else ""
                s2 = " " + dp(r) if r else ""
                return s1 + n2w[div] + s2

        return dp(num)
