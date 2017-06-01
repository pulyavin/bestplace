import first

def test_range_original():
    a = 1
    b = 2
    c = 5

    assert first.median3(a, b, c) == b

def test_range_shuffled():
    a = 2
    b = 5
    c = 1

    assert first.median3(a, b, c) == a