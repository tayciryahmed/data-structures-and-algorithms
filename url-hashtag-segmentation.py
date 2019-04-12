import sys 

class DeterministicUrlHashtagSegmentation:
    
    def __init__(self):
        pass
    
    def tokenize(self, text, words):
        curr = 0 
        tokenized_words = []

        for ind, char in enumerate(text):

            if text[:curr] in words:
                tokenized_words.append(text[:curr])
                text = text [curr:]
                curr = 0
            
            curr += 1
        
        if text in words:
            tokenized_words.append(text)
        
        return tokenized_words
            

    def solve(self, text, words):
        if text.startswith('#'):
            tokenized = self.tokenize(text[1:], words)
            if len(tokenized) > 0:
                return " ".join(self.tokenize(text[1:], words)) 
            else:
                return text[1:]
        elif '.' in text:
            tokenized = self.tokenize(text[:text.index('.')], words)
            if len(tokenized) > 0:
                return " ".join(tokenized) 
            else:
                return text[:text.index('.')]
            
        return None

if __name__ == "__main__":
    input_text = sys.stdin.read()
    words = open("words.txt").read().split('\n')
    solution = DeterministicUrlHashtagSegmentation()
    for text in input_text.split('\n'):
        response = solution.solve(text, words)
        if response:
            print(response)
