def only_evens(list):
    even_list = []
    for num in list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            None
    return even_list

num_list = [1, 2, 3, 4, 5, 6]
print(only_evens(num_list))