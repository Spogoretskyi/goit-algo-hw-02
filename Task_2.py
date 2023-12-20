from collections import deque


def is_palindrome(input_str):
    clean_str = input_str.lower().replace(" ", "")
    char_queue = deque(clean_str)

    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False

    return True


input_string = "littil"
result = is_palindrome(input_string)

input_string = "little"
result = is_palindrome(input_string)

input_string = "littil "
result = is_palindrome(input_string)

input_string = "littil 1"
result = is_palindrome(input_string)

if result:
    print(f'String "{input_string}" - is palindrome.')
else:
    print(f'String "{input_string}" - is not palindrome.')
