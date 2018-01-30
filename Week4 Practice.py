def nfruits(fruitBag, roadFruit):
    for letter in roadFruit:
        if letter in fruitBag.keys():
            fruitBag[letter] -= 1
    for key in fruitBag.keys():
        if key not in roadFruit:
            fruitBag[key] += 1

    return fruitBag

#Checking the delete.
