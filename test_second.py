import second

def test_range_8():
    arr = [9, 2, 3, 5, 7, 1, 4, 6]
    truth = 8

    assert second.findMissing(arr) == truth

def test_range_6():
    arr = [2, 3, 5, 7, 1, 4]
    truth = 6

    assert second.findMissing(arr) == truth