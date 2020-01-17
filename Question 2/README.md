# To Run: 
        Navigate to src
        Test file is prices.txt in the data directory

        For find_pair.py:
            python find_pair.py <file> <card_value>

        For find_triple:
            python find_triple.py <file> <card_value>
    

# Solution Notes: 
        The general logic behind both answers is that we can utilize the sorted nature 
        of the input to simplify our search for a pair by incrementing or decrementing
        left and right indice values for the array we assemble from prices.txt. We can 
        increase the value of our current sum by incrementing the left index and decrease
        the current sum by decrementing our right index by one. We update our pair_found 
        only when the remainder from the difference of card_val and cur_sum is less than 
        our smallest remainder. The solution does rely on correct file input but can be
        modified to do robust testing of input first.

# RunTime:
    find_pair.py:
        Runtime complexity will be at worst case O(N) because we only make one pass 
        over the assembled list at most.
    find_triple.py
        Runtime complexity is increased by a factor of N to O(N^2) because we now
        loop N times over our previous solution to provide combinations with the
        additional third item. 

# Memory Optimization:
    In order to decrease the memory needed to find a pair within the constaints we 
    could implement lazy reading of the file. Instead of generating a full array 
    we could utilize file pointers that would work just like our left and right 
    indice pointers. These would keep track of the beggining of the file and the 
    end of the file and thus would be our least expensive item and our most expensive
    item. If the sum of the two read in values is greater than the card value we 
    could decrement the end pointer by one or if the value is less than the card
    value we could increment the beggining pointer and then read in the new value.

# Test Output:
    python find_pair.py ../data/prices.txt 2500
    Candy Bar   500 ,  Earmuffs   2000

    python find_pair.py ../data/prices.txt 2300
    Paperback Book   700 ,  Headphones   1400

    python find_pair.py ../data/prices.txt 10000
    Earmuffs   2000 ,  Bluetooth Stereo   6000

    python find_pair.py ../data/prices.txt 1100
    Not Possible

    python find_triple.py ../data/prices.txt 10000
    Earmuffs   2000 ,  Bluetooth Stereo   6000 ,  Headphones   1400

    python find_triple.py ../data/prices.txt 2500
    Paperback Book   700 ,  Detergent   1000 ,  Candy Bar   500

    python find_triple.py ../data/prices.txt 2000
    Not Possible




