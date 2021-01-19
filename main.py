def sumBetween(x, y):

    total = 0

    for i in range (x, y):
        total = total + i

    return total

print (sumBetween(0, 10))