def cels_to_fahr(cels):
    new_temp = (cels * 9/5) + 32
    return new_temp

print(cels_to_fahr(10))

def fahr_to_cels(fahr):
    new_temp = (fahr - 32) * 5/9
    return new_temp
print(fahr_to_cels(10))