class Solution:
    def numberOfSteps (self, num: int) -> int:
        if not num:
            return 0
        res = 0
        while(num):
            res += 2 if (num & 1) else 1
            num >>= 1;

        return res - 1
