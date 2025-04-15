def palindrome(word):
    if word == "":
        return None
    if not isinstance (word, str):
        raise AttributeError("Only string values are accepted!")
    
    word = word.lower()
    reversed_word = word[::-1]
    print(reversed_word)
    
    if reversed_word == word:
        return True
    return False
# print(palindrome(""))
# print(palindrome("[121]"))
print(palindrome("apa"))
# print(palindrome(1234))


def palindrome(word):
    if word == "":
        return None
    if not isinstance (word, str):
        raise AttributeError("Only string values are accepted!")
    
    word = word.lower()
    
    reversed_word = "".join(reversed(word))
    print(reversed_word) 
    
    if reversed_word == word:
        return True
    return False

print(palindrome("olleh"))


def is_palindrome_iterative(word):
    # Check if the word is empty
    if word == "":
        return None  # No word to check, return None

    # Change all letters to lowercase so we can compare them easily
    word = word.lower()

    # Set two pointers: one at the start, one at the end
    left = 0
    right = len(word) - 1

    # Keep checking letters while the left pointer is before the right one
    while left < right:
        # If the letters at left and right don't match, it's not a palindrome
        if word[left] != word[right]:
            return False
        # Move the left pointer to the right
        left += 1
        # Move the right pointer to the left
        right -= 1

    # If all letters matched, it's a palindrome
    return True

