from calc.calc import Calc

def test_add_two_numbers():
    c = Calc() # The Calc is instantiated 

    expected = 9
    actual = c.add(4, 5)

    assert actual == expected

def test_add_three_numbers():
    c = Calc()

    expected = 15
    actual = c.add(4, 5, 6)

    assert actual == expected    