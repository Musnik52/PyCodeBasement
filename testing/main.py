from Calculator import *
from salinput import *
import pytest

@pytest.mark.parametrize("x,y,z", [(10, 20, 30), (40, 50, 90)])
def test_add_parameters(x, y, z):
    calc = Calculator()
    actual = calc.add(x, y)
    expected = z
    assert actual == expected

def test_add_two_small_numbers():
    calc = Calculator()
    actual = calc.add(3, 4)
    expected = 7
    assert actual == expected

def test_sub_two_small_numbers():
    calc = Calculator()
    actual = calc.sub(9, 7)
    expected = 2
    assert actual == expected

def test_mul_two_small_numbers():
    calc = Calculator()
    actual = calc.mul(3, 4)
    expected = 12
    assert actual == expected

def test_div_two_small_numbers():
    calc = Calculator()
    actual = calc.div(28, 4)
    expected = 7
    assert actual == expected

def test_div_by_zero_expect_error():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(28, 0)

def test_sal_correct():
    salary = SalaryInputs()
    amount = 19990.0
    assert salary.get_salary(amount) == amount * 2

#to test: C:\git\pyCodeBasement\testing> python -m pytest main.py