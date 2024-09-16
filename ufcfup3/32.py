def add_one_to_ascii(word):
    result = ""

    for char in word:
        new_ascii = ord(char) + 1
        result += chr(new_ascii)

    return result


user_word = input("")

result_word = add_one_to_ascii(user_word)

print(f"{result_word}")