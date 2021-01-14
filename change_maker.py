import math

def bills(charge, payment):
    charge = int(math.ceil(charge))
    payment = int(math.floor(payment))
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
    
def coins(charge, payment):
    coins_tuple = ()
    bills_charge = int(charge)
    bills_payment = int(payment)
    coins_payment = payment - bills_payment + 1
    coins_charge = charge - bills_charge
    coins = int(abs(coins_charge - coins_payment) * 100)
    if coins / 25 > 0:
        quarters = (coins - (coins % 25))/25
        coins_tuple = coins_tuple + (int(quarters),)
        coins -= 25 * quarters
    if coins / 10 > 0:
        dimes = (coins - (coins % 10))/10
        coins_tuple = coins_tuple + (int(dimes),)
        coins -= 10 * dimes
    if coins / 5 > 0:
        nickles = (coins - (coins % 5))/5
        coins_tuple = coins_tuple + (int(nickles),)
        coins -= 5 * nickles
    if coins / 1 > 0:
        pennies = (coins - (coins % 1))
        coins_tuple = coins_tuple + (int(pennies),)
        coins -= 1 * pennies
    return(coins_tuple)

def change_calc(charge_amt, payment_amt):
    charge = charge_amt
    payment = payment_amt
    return(bills(charge, payment), coins(charge, payment))

print(change_calc(98.21, 100.99))
# print(bills(98.01, 100.01), "bills func")
# print(coins(98.21, 100), "coins func")

