def random_list(i):
    """Random list of number from 0 - 100"""
    import random
    num_list = sorted(random.sample(range(0, 100), i))
    return num_list

def sum_pair_search(lst,number):  # O(log N) Binary Search
    """This is the function that do the binary search and the prove the calculation"""

    # The list must be sorted!! Important!!!!
    #O(log N)
    num_lst = random_list(lst)

    low = 0                     # index of the lowest number
    high = len(num_lst) - 1     # index of the highest number

    # Binary search
    while low <= high:
        mid = (low + high) // 2
        if num_lst[low] + num_lst[high] == number:    # Check if the pair are added up to the target number.
            print('Found It!')
            print(num_lst[low],'+',num_lst[high],'=',number)
            return True
        elif number < num_lst[mid]:             # Adjust high : Go search lower half portion
            high = mid - 1
        else:
            low = mid + 1                       # Adjust low : Go search upper half portion
    print('No Pair Found in this Particular list of number.')
    return False

def main():
    while True:
        num = random_list(20)
        if sum_pair_search(num,20):
            break

if __name__ == '__main__':
    main()


