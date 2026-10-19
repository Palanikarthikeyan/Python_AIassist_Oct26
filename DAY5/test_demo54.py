import pytest

@pytest.fixture
def input_data():
    var = 39
    return var

def test_divisible_by_3(input_data):
    assert input_data % 3 == 0
    
def test_divisible_by_6(input_data):
    assert input_data % 6 == 0