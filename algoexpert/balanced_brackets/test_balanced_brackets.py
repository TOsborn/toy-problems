from balanced_brackets import balancedBrackets

def test_balancedBrackets_sample():
    string = "([])(){}(())()()"

    assert balancedBrackets(string) is True
    
def test_balancedBrackets_empty():
    string = ""

    assert balancedBrackets(string) is True

def test_balancedBrackets_invalid():
    string = "([])(){}(())()())"

    assert balancedBrackets(string) is False


def test_balancedBrackets_other_character():
    string = "([])(){}(()a)()()"

    assert balancedBrackets(string) is True
