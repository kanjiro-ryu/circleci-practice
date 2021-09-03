import pytest 
from src.math import addition

def test_addition():
        actual = addition(3,4)
        assert actual == 7

