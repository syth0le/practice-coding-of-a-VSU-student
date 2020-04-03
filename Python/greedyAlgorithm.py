nominals = [5000, 2000, 1000, 500, 200, 100, 50, 10, 5, 2, 1]
print('Enter value in cents: ', end='')
change = int(input())
i = 0
localArr = []  # save here coins counting results
while change != 0:  # create while for change's counting
    if change >= nominals[i]:
        localArr.append(nominals[i])  # save coins to array
        change -= nominals[i]
    else:
        i += 1  # adding 1 to iterating in 'nominals'
# add all coins to dict and counting them:
coinDict = {}
for coin in localArr:
    if coin in coinDict:
        coinDict[coin] += 1
    else:
        coinDict[coin] = 1
# restructuring our output
print("\nChange result:")
for coin in coinDict:
    if coin >= 100:
        print('Coin value - %d dollar, quantity - %d.' % ((coin / 100), coinDict[coin]))
    else:
        print('Coin value - %d cents, quantity - %d.' % (coin, coinDict[coin]))
