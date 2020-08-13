def has_palindrome_permutation(the_string):

    freq = {}
    
    count_1 = 0
    
    for c in the_string:
        freq[c] = (freq.setdefault(c, 0) + 1 ) % 2
        if freq[c] == 1:
            count_1 += 1
        else:
            count_1 -= 1
        

    return count_1 <= 1
