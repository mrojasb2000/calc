from calc.calc import Calc

def test_add_two_numbers():
    c = Calc() # The Calc is instantiated 

    expected = 9
    actual = c.add(4, 5)

    assert actual == expected