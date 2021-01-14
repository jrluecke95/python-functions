def largest_num(list):
    large_num = list[0]
    for num in list:
        if num > large_num:
            large_num = num 
    return large_num

print(largest_num([1, 2, 3, 4, 5]))