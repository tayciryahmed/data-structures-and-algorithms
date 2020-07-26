class Solution(object):
    def buddyStrings(self, A, B):
        if len(A) != len(B): return False
        if A == B and len(set(A)) <= len(A)-1 : return True
        
        
        pairs = []
        for a, b in zip(A, B):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3: return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
