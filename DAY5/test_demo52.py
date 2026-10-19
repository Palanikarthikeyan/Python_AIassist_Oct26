import pytest
import sys

@pytest.mark.skip
def test_payment():
    assert 100 + 50 == 150

def test_add():
    assert 10 + 20 == 30

def test_sub():
    assert 10 - 5 == 5
    
@pytest.mark.skipif(sys.platform != "linux",reason="This test require Linux")
def test_linux_features():
    assert True
        
@pytest.mark.xfail(reason="known bug")
def test_bug_feature():
    assert 10 - 5 == 10
