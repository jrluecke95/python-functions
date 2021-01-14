def only_evens(list):
    even_list = []
    for num in list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

num_list = [1, 2, 3, 4, 5, 6]
print(only_evens(num_list))

def only_odds(list):
    odd_list = []
    for num in list:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

print(only_odds(num_list))