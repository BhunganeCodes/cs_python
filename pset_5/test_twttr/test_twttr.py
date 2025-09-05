from twttr import shorten

def test_shorten():
    assert shorten("Hey!") == "Hy!"
    assert shorten("CS50...") == "CS50..."
    assert shorten("Hungryy") == "Hngryy"