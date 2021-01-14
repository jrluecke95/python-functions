def even(num):
    if num % 2 == 0:
        print("you're number is even")
        return True
    else:
        return False

def odd(num):
    if even(num) is False:
        return ("you're number is odd")
    
print(odd(3))
