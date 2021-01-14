string_list = ["this", "is", "a", "list"]

def shortest_string(list):
    short_string = list[0]
    for string in list:
        if len(string) < len(short_string):
            short_string = string
    return short_string

print(shortest_string(string_list))