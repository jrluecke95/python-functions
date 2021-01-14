def bills(charge, payment):
    charge = int(charge)
    payment = int(payment)
    bills_tuple = ()
    if payment >= charge:
        change = payment - charge
    else:
        return 0
    if change / 100 > 0:
        hund = (change - (change % 100))/100
        bills_tuple = bills_tuple + (int(hund),)
        change -= 100 * hund
    if change / 50 > 0:
        fifty = (change - (change % 50))/50
        bills_tuple = bills_tuple + (int(fifty),)
        change -= 50 * fifty
    if change / 20 > 0:
        twenty = (change - (change % 20))/20
        bills_tuple = bills_tuple + (int(twenty),)
        change -= 20 * twenty
    if change / 10 > 0:
        tens = (change - (change % 10))/10
        bills_tuple = bills_tuple + (int(tens),)
        change -= 10 * tens
    if change / 5 > 0:
        fives = (change - (change % 5))/5
        bills_tuple = bills_tuple + (int(fives),)
        change -= 5 * fives
    if change / 1 > 0:
        singles = (change - (change % 1))
        bills_tuple = bills_tuple + (int(singles),)
        change -= 1 * singles
    return(bills_tuple)
    

print(bills(350, 497))


# def change(charge, payment):

# def make_change(total_charge, payment):

# # test = (1, 2)
# # test2 = test + (9,)
# # print(test2)sv