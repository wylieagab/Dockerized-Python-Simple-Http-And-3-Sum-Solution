"""

find_triple.py
@author: wylieagab

"""

import sys



def find_triple(filename, card_val):
    """
    Because we know the list is sorted we can utilize pointers on either side
    to increase or decrease our temporary purchasing sum. Adding an additional 
    search query to find_pair increases runtime by a multiple of N. Thus runtime
    is O(n^2).
    """
    item_list = file_to_list(filename, card_val)
    left_index = 0
    right_index = len(item_list) - 1
    item_index = 0
    price_index = 1
    triple_found = [None, None, None]
    smallest_remainder = float('inf') #difference of gift card val and current sum
    
    for i in range(len(item_list)-2):
        left_index = i+1
        right_index = len(item_list) - 1
        
            
        while(left_index < right_index):
            # sum of prices of left and right item
            cur_sum = item_list[left_index][price_index] + item_list[right_index][price_index] + item_list[i][price_index]
            remainder = card_val - cur_sum
        
            # checks to see if the remainder is the smallest remainder and then updates right or left index
            if remainder < smallest_remainder and remainder >= 0:
                smallest_remainder = remainder
                triple_found[0] = item_list[left_index]
                triple_found[1] = item_list[right_index]
                triple_found[2] = item_list[i]
                if remainder == 0:
                    return print_result(triple_found, item_index, price_index)
            if cur_sum > card_val:
                right_index = right_index - 1
            elif cur_sum < card_val:
                left_index = left_index + 1
    
    return print_result(triple_found, item_index, price_index)

def print_result(triple_found, item_index, price_index):
    """
    Checks if triple_found is not None and then prints the resulting
    interpretted answer
    """
    if triple_found[0]:
        item, price = triple_found[0][item_index], triple_found[0][price_index]
        item_1, price_1 = triple_found[1][item_index], triple_found[1][price_index]
        item_2, price_2 = triple_found[2][item_index], triple_found[2][price_index]
        print(item, " ", price, ", ", item_1, " ", price_1, ", ", item_2, " ", price_2)
    else:
        print("Not Possible")

def file_to_list(filename, card_val):
    """
    Reads in the sorted file and creates a list of tuples (item, price)
    """
    item_list = []

    with open(filename, 'r') as f:
        for line in f:
            item, price = line.split(',')
            item_list.append((item, int(price)))

    return item_list



if __name__ == "__main__":
    find_triple(sys.argv[1], int(sys.argv[2]))
