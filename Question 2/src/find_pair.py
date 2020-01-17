"""

find-pair.py
@author: wylieagab

"""

import sys



def find_pair(filename, card_val):
    """
    Because we know the list is sorted we can utilize pointers on either side
    to increase or decrease our temporary purchasing sum. Runtime is thus in 
    the worst case O(N) where N is the amount of items. 
    """
    item_list = file_to_list(filename, card_val)
    left_index = 0
    right_index = len(item_list) - 1
    item_index = 0
    price_index = 1
    pair_found = [None, None]
    smallest_remainder = float('inf') #difference of gift card val and current sum
    
    
    while(left_index != right_index):
        #sum of prices of left and right item
        cur_sum = item_list[left_index][price_index] + item_list[right_index][price_index]
        remainder = card_val - cur_sum
        
        # checks to see if the remainder is the smallest remainder and then updates right or left index
        if remainder < smallest_remainder and remainder >= 0:
            smallest_remainder = remainder
            pair_found[0] = item_list[left_index]
            pair_found[1] = item_list[right_index]
            if remainder == 0:
                break
        if cur_sum > card_val:
            right_index = right_index - 1
        elif cur_sum < card_val:
            left_index = left_index + 1
    
    #checks if pair_found is not None and then prints the result 
    if pair_found[0]:
        item, price = pair_found[0][item_index], pair_found[0][price_index]
        item_1, price_1 = pair_found[1][item_index], pair_found[1][price_index]
        print(item, " ", price, ", ", item_1, " ", price_1)
    else:
        print("Not Possible")

def file_to_list(filename, card_val):
    """
    Reads in file to a list of tuples (item, price)
    """
    item_list = []

    with open(filename, 'r') as f:
        for line in f:
            item, price = line.split(',')
            item_list.append((item, int(price)))

    return item_list



if __name__ == "__main__":
    find_pair(sys.argv[1], int(sys.argv[2]))
