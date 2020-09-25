class Solution:
    def decodeString(self, s: str) -> str:
        counts = []
        strings = []
        
        res = ""
        index = 0
        
        while index < len(s):
            if s[index].isdigit() :
                count = 0 
                while s[index].isdigit():
                    count = 10 * count + int(s[index])
                    index += 1
                counts.append(count)
            elif s[index] == '[':
                strings.append(res)
                res = ""
                index += 1                
            elif s[index] == ']':
                tmp = strings.pop()
                count = counts.pop()
                for i in range(count):
                    tmp += res
                
                res = tmp
                index += 1
                
            else:
                res += s[index]
                index += 1 
                
        return res 
