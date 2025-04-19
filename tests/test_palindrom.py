from palindrome.palindrome import palindrome
import pytest


# example input 1: ""
# expected output 1: False

# example input 2: "KaYak"
# expected output 2: True

# example input 3:  "papa"
# expected output 3: False

# example input 4: 12321
# expected output 4: TypeError: Only string values are accepted!




# test 1
def test_if_the_string_is_empty():
    #Arrange
    word = ""
    # Act
    result = palindrome(word)
    #Assert
    assert result is None
    
# test 2  
def test_change_string_characters_to_lower_case():
    #Arrange
    word = "KaYak"
    #Act
    result = palindrome(word)
    #Assert
    assert result == True
    
# test 3
def test_if_word_is_not_palindrome():
    #Arrange
    word = "papa"
    #Act
    result = palindrome(word)
    #Assert
    assert result == False
    
# test 4
def test_if_word_is_palindrome():
    #Arrange
    word = "apa"
    #Act
    result = palindrome(word)
    #Assert
    assert result == True

# test 5
def test_if_the_word_is_string():
    #Arrange
    word = 1234
    #Act
    with pytest.raises(TypeError) as error:
        result = palindrome(word)

    assert str(error.value) == "Only string values are accepted!"
