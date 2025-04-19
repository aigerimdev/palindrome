def palindrome(word):
    if not isinstance (word, str):
        raise AttributeError("Only string values are accepted!")
        
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
# print(palindrome


Logic of code:

1. Define a function called palindrome that takes one argument called word.
2. Check the data type of word. It should be a string:
– Otherwise, raise an error.
1. If the string is empty:
– Return None.
1. Convert the word to lowercase.
2. Set two pointers: one at the start called left, and one at the end called right.
3. While left is less than right, start a loop:
– If the characters at left and right are not equal:
– Return False.
– Otherwise, increment left and decrement right.
1. Return True if all characters matched.



The time complexity of the pointer solution is:

👉 O(n), where n is the length of the string.

Because:

You check each character once from both ends using left and right.
The space complexity is:

👉 O(1), because you use only a few variables (left, right, etc.), no extra memory that grows with input.