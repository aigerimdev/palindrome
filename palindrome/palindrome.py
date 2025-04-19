def palindrome(word):
    if not isinstance (word, str):
        raise TypeError("Only string values are accepted!")
        
    if word == "":
        return None
    
    word = word.lower()
        
# two pointers: one at the start, one at the end 
    left_pointer = 0
    right_pointer = len(word)-1
    
    while left_pointer < right_pointer:
        if word[left_pointer] != word[right_pointer]:
            return False
        left_pointer += 1
        right_pointer -= 1
        
    return True
# print(palindrome("apa"))
# print(palindrome("Apa"))
# print(palindrome("kayak"))

# print(palindrome(12334))
print(palindrome('a'))
# print(palindrome(""))

