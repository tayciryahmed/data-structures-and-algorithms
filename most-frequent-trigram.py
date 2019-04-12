import sys

class MostFrequentTrigram:
    
    def __init__(self):
        pass
    
    def solve(self, text):
        text = text.lower() 
        tokenized_sentences = [w.split() for w in text.split('.')]
        
        trigrams = {}
        
        for sentence in tokenized_sentences:
            for i, w in enumerate (sentence):
                if i + 2 < len(sentence):
                    if ' '.join(sentence[i:i+3]) not in trigrams.keys():
                        trigrams[' '.join(sentence[i:i+3])] = 1 
                    else:
                        trigrams[' '.join(sentence[i:i+3])] += 1
        max_trigram = max(trigrams.keys(), key=(lambda k: trigrams[k]))
        
        if trigrams[max_trigram] == 1:
            return ' '.join(tokenized_sentences[0][:3])

        return max_trigram

if __name__ == "__main__":
    input_text = sys.stdin.read()
    solution = MostFrequentTrigram()
    response = solution.solve(input_text)
    print(response)
