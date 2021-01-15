

def bills(charge, payment):
    #next two lines turn floats to ints for coin calc later
    bills_charge = int(charge)
    bills_payment = int(payment)
    bills_tuple = ()
    #calculating coins for rounding errors that can occur - rounding the float to 2 points in the process
    coins_payment = round((payment - bills_payment), 2)
    coins_charge = round((charge - bills_charge), 2)
    #following if statement checks for need for "rounding"
    if coins_payment < coins_charge:
        bills_charge += 1
    # setting change up for the next if statements
    change = bills_payment - bills_charge
    #following if/else statements see if certain bills are needed, subtracts them from total, and adds number of bills needed to tuple - else statements add 0's to tuple after change = 0
    if change / 100 > 0:
        hund = (change - (change % 100))/100
        bills_tuple = bills_tuple + (int(hund),)
        change -= 100 * hund
    else:
        bills_tuple = bills_tuple + (0,)
    if change / 50 > 0:
        fifty = (change - (change % 50))/50
        bills_tuple = bills_tuple + (int(fifty),)
        change -= 50 * fifty
    else:
        bills_tuple = bills_tuple + (0,)
    if change / 20 > 0:
        twenty = (change - (change % 20))/20
        bills_tuple = bills_tuple + (int(twenty),)
        change -= 20 * twenty
    else:
        bills_tuple = bills_tuple + (0,)
    if change / 10 > 0:
        tens = (change - (change % 10))/10
        bills_tuple = bills_tuple + (int(tens),)
        change -= 10 * tens
    else:
        bills_tuple = bills_tuple + (0,)
    if change / 5 > 0:
        fives = (change - (change % 5))/5
        bills_tuple = bills_tuple + (int(fives),)
        change -= 5 * fives
    else:
        bills_tuple = bills_tuple + (0,)
    if change / 1 > 0:
        singles = (change - (change % 1))
        bills_tuple = bills_tuple + (int(singles),)
        change -= 1 * singles
    else:
        bills_tuple = bills_tuple + (0,)
    return(bills_tuple)
    
def coins(charge, payment): 
    coins_tuple = ()
    #2 lines below gives me whole number of bills - converts float to int
    bills_charge = int(charge) 
    bills_payment = int(payment) 
    #next 2 give me change by subtracting bills from total amt given and rounding float to 2 places
    coins_payment = round((payment - bills_payment), 2)
    coins_charge = round((charge - bills_charge), 2)
    #next if/elif check payment/charge amount and see if i need to add 1 so that the change can be proper (accounting for situations where you could give too much change because of bill amt being 10 but really needing 9.75 for example)
    if coins_payment < coins_charge:
        coins_payment += 1
        coins = int((coins_payment - coins_charge) * 100)
    elif coins_payment >= coins_charge:
        coins = int((coins_payment - coins_charge) * 100)
    #following if statements find which coinns are needed, what amounts, and then add said amount to the tuple - else statements add 0 to tuple once coins equals 0
    if coins / 25 > 0:
        quarters = (coins - (coins % 25))/25
        coins_tuple = coins_tuple + (int(quarters),)
        coins -= 25 * quarters
    else:
        coins_tuple = coins_tuple + (0,)
    if coins / 10 > 0:
        dimes = (coins - (coins % 10))/10
        coins_tuple = coins_tuple + (int(dimes),)
        coins -= 10 * dimes
    else:
        coins_tuple = coins_tuple + (0,)
    if coins / 5 > 0:
        nickles = (coins - (coins % 5))/5
        coins_tuple = coins_tuple + (int(nickles),)
        coins -= 5 * nickles
    else:
        coins_tuple = coins_tuple + (0,)
    if coins / 1 > 0:
        pennies = (coins - (coins % 1))
        coins_tuple = coins_tuple + (int(pennies),)
        coins -= 1 * pennies
    else:
        coins_tuple = coins_tuple + (0,)
    return(coins_tuple)

def change_calc(charge_amt, payment_amt):
    charge = charge_amt
    payment = payment_amt
    return(bills(charge, payment), coins(charge, payment))

print(change_calc(90.51, 100.49))


