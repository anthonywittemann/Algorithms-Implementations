# Anthony Wittemann
# HW 2 Pr 2 Cashier's Algo

def main():
    coinage = [1, 5, 10, 25, 100, 500, 1000, 2000] #can be modified
    cents = 123456 				   #can be modified
    change = cashier(cents, coinage)
    for c in range(len(change)):
        print("Number of",coinage[c], "coins:",change[c])

def cashier(cents, coinage):
    coin = len(coinage) - 1
    change = list(range(coin + 1))
    remainder = cents
    
    while coin >= 0:
        change[coin] = remainder // coinage[coin]
        remainder = remainder % coinage[coin]
        coin -= 1

    return change

main()
