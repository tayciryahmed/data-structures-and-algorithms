
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    i, j = 0, 0
    
    for k in range(len(served_orders)):
        if i < len(take_out_orders) and served_orders[k] == take_out_orders[i]:
            i += 1
        elif j < len(dine_in_orders) and served_orders[k] == dine_in_orders[j]:
            j += 1
        else:
            return False

    return i == len(take_out_orders) and j == len(dine_in_orders)

