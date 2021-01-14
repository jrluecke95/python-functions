string_list = ["this", "is", "another", "list"]

def longest_string(list):
    long_string = list[0]
    for string in list:
        if len(string) > len(long_string):
            long_string = string
    return long_string

print(longest_string(string_list))