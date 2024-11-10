import pytest

@pytest.mark.one
def test_one():
    x=5
    y=6
    assert x==y

@pytest.mark.two
def test_two():
    x=5
    y=6
    assert x+1 == y
