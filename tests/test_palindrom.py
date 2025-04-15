from palindrome.palindrome import palindrome

def test_if_the_string_is_empty():
    #Arrange
    word = ""
    # Act
    result = is_palindrome(word)
    #Assert
    assert result is None
    
def test_change_string_to_lover_case():
    #Arrange
    word = "KaYak"
    #Act
    result = is_palindrome(word)
    #Assert
    assert result == "Yes"

def test_if_word_is_not_palindrom():
    #Arrange
    word = "papa"
    #Act
    result = is_palindrome(word)
    #Assert
    assert result == "No"

def test_if_word_is_palindrom():
    #Arrange
    word = "apa"
    #Act
    result = is_palindrome(word)
    #Assert
    assert result == "Yes"