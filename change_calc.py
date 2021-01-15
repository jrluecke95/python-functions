test_tuples = (
    (3, 0, 1, 1, 0, 1),
    (3, 1, 0, 2)
)

# print(test_tuples[0]) = (3, 0, 1, 1, 0, 1)

def bills(tuple):
    bills_total = 0
    for i in range(len(tuple[0])):
        if i == 0:
            bills_total += tuple[0][i] * 100
        if i == 1:
            bills_total += tuple[0][i] * 50
        if i == 2:
            bills_total += tuple[0][i] * 20
        if i == 3:
            bills_total += tuple[0][i] * 10
        if i == 4:
            bills_total += tuple[0][i] * 5
        if i == 5:
            bills_total += tuple [0][i] * 1
    return bills_total

def coins(tuple):
    coins_total = 0
    for i in range(len(tuple[1])):
        if i == 0:
            coins_total += round((tuple[1][i] * .25), 2)
        if i == 1:
            coins_total += round((tuple[1][i] * .10), 2)
        if i == 2:
            coins_total += round((tuple[1][i] * .05), 2)
        if i == 3:
            coins_total += round((tuple[1][i] * .01), 2)
    return coins_total

def change_calc(tuples):
    return bills(tuples) + coins(tuples)

print(change_calc(test_tuples))