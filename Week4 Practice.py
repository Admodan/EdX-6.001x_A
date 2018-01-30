def nfruits(fruitBag, roadFruit):
    for letter in roadFruit:
        if letter in fruitBag.keys():
            fruitBag[letter] -= 1
    for key in fruitBag.keys():
        if key not in roadFruit:
            fruitBag[key] += 1

    return fruitBag

#making some changes here. Let's see what happens. 
#Good thing you are the fucking man.

#Good job on being the man.
