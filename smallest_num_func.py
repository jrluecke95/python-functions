num_list = [1, 2, 3, 4, 5, -1]

def smallest_num(list):
    small_num = list[0]
    for num in list:
        if num < small_num:
            small_num = num
    return small_num

print(smallest_num(num_list))
