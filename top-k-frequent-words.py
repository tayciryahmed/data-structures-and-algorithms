from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words).most_common(len(words))
        words.sort(key=lambda x: (-x[1], x[0]))
        return [words[i][0] for i in range(len(words)) if i <k]
        
