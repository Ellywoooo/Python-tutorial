from hello import hello

def test_default():
    assert hello() == "hello, Elly"

def test_arugment():
    assert hello("Elly") == "hello, Elly"