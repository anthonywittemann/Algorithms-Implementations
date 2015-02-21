# Anthony Wittemann
# HW 2 Pr 2 Cashier's Algo

def main():
    cashier(2000)

def cashier(nCents):
    coinsInAscendingValue = [1,7,35,140]
    selectedCoins = [0,0,0,0]
    while nCents > 0 and currentCoin > -1:
        currentCoin = len(coinsInAscendingValue) - 1
        selectedCoins[currentCoin] = nCents // coinsInAscendingValue[currentCoin]
        nCents -= (selectedCoins[currentCoin] * coinsInAscendingValue[currentCoin])
        currentCoin -= 1
    for c in selectedCoins:
        print(c)


main()
