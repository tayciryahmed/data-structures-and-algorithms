def solution(k, keywords, reviews):
  reviews = [set(review.lower().split()) for review in reviews]
  keywords = {x: 0 for x in keywords}
  for review in reviews:
    for keyw in keywords:
      if keyw in review:
        keywords[keyw] += 1
  keywords = [(x, y) for x,y in keywords.items()]
  keywords.sort(key=lambda x: (-x[1], x[0]))
    
  return [x[0] for x in keywords][:k]
  
 
 def solution(k, keywords, reviews):
  frequencies = {}
  for review in reviews:
    review = review.lower()
    encountered_words = set()
    for reviewWord in review.split():
      reviewWord not in encountered_words and reviewWord in keywords:
        frequencies.setdefault(reviewWord, 0)
        frequencies[reviewWord] += 1
        encountered_words.add(reviewWord)
  frequencies = [(x, y) for x,y in keywords.items()]
  frequencies.sort(key=lambda x: (-x[1], x[0]))
  return [x[0] for x in frequencies][:k]
        
 
