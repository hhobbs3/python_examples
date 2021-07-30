# test_with_pytest.py
# pip install pytest
# pip install pytest-cov
# run pytest to test cases


import classes

def test_always_fails():
    assert False

def test_always_passes():
    assert True
def test_greating():
    g = classes.Greatings()
    assert g.greating() == "Greatings"

def test_hello_world():
    h = classes.HelloWorld()
    assert h.greating() == "Greatings"
    assert h.hello_world() == "Hello, World"