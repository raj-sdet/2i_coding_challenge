import pytest
# Firstly remove duplicates from the list of whole numbers to satify this condition; "Each array element can only be used in one pair"

def remove_duplicates_from_list_of_whole_numbers(list_of_whole_numbers):
    return list(dict.fromkeys(list_of_whole_numbers)) # this will remove duplicates from the list if there are any

def count_sum_of_pairs_from_given_list(list_of_whole_numbers, x):
    pairs = []
    list_of_whole_numbers = remove_duplicates_from_list_of_whole_numbers(list_of_whole_numbers)
    for i in range(len(list_of_whole_numbers)): # index i will go from 0 to len(list_of_whole_numbers)
        for j in range(len(list_of_whole_numbers) - 1, i, -1): # index j will go from len(list_of_whole_numbers) to i
            if list_of_whole_numbers[i] + list_of_whole_numbers[j] == x:
                pairs.append((list_of_whole_numbers[i], list_of_whole_numbers[j]))
    return pairs

# test cases using pytest to check the correctness of the above solution from the example given in the problem statement

@pytest.mark.parametrize("arr, sum_value, expected", [([3, 4, 5, 6], 1, []), 
                                                      ([0, 15, 32, 2000, 15000], 15, [(0, 15)]),
                                                      ([1, 1, 10, 32, 41], 42, [(1, 41), (10, 32)])
                                                      ]) 
def test_count_sum_of_pairs_from_given_list(arr, sum_value, expected):
    assert count_sum_of_pairs_from_given_list(arr, sum_value) == expected