from bank import value

def test_hello():
    assert value("hello") == 0

def test_starting_h():
    assert value("hey") == 20
    assert value("hi") == 20

def test_any_greeting():
    assert value("what's up?") == 100
    assert value("yo") == 100