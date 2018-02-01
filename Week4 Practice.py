def nfruits(fruitBag, roadFruit):
    assert not len(fruitBag) == 0, 'No fruit in the bag'
    assert not len(roadFruit) == 0, 'No road fruit eaten'
    for letter in roadFruit:
        if letter in fruitBag.keys():
            fruitBag[letter] -= 1
    for key in fruitBag.keys():
        if key not in roadFruit:
            fruitBag[key] += 1

    return max(fruitBag.values())