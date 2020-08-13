def get_products_of_all_ints_except_at_index(int_list):
    
    if len(int_list) <=1: 
        raise Exception()

    ans = [1] * len(int_list) 
    
    # left products 
    for i in range(1, len(int_list)):
        ans [i] = ans[i-1] * int_list[i-1]
    
    R = 1
    for i in range(len(int_list)-1, -1, -1):
        ans[i] = ans[i] * R
        R = R * int_list[i]
    

    return ans

