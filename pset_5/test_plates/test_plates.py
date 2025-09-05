from plates import is_valid

def test_length():
    assert is_valid("AB") == True
    assert is_valid("A") == False
    assert is_valid("ABC1234") == False

def test_two_letters():
    assert is_valid("50") == False
    assert is_valid("CS50") == True

def test_alnum():
    assert is_valid("CS50!") == False
    assert is_valid("AB12") == True

def test_numbers():
    assert is_valid("CS50P") == False
    assert is_valid("CS50") == True
    assert is_valid("TH00") == False