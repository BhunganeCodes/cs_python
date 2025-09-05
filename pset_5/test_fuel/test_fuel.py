from fuel import convert, gauge
from pytest import raises

def test_convert():
    assert convert("1/10") == 10
    assert convert("50/100") == 50

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(55) == "55%"

def test_exceptions():
    with raises(ValueError):
        convert("cat/dog")