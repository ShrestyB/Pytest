import pytest

@pytest.fixture

def numbers():
    x = 10
    y = 20
    z = 25
    return [x,y,z]

def test_number1(numbers):
    a = 15
    assert numbers[0] == a

def test_number2(numbers):
    b = 20
    assert numbers[1] == b

def test_number3(numbers):
    c = 25
    assert numbers[2] == c  
