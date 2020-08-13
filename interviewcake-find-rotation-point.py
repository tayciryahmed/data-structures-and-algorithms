def find_rotation_point(words):

    start, end = 0, len(words) - 1
    
    while start +1 != end :
        mid = (end+start) // 2
        if words[start] < words[mid]:
            start = mid
        else:
            end = mid

    return end
