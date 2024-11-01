text = "Zldgrprvf gr cdvcbiurzdqld"

text = text.lower()

letters = []

def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                encrypted_text += chr((shifted - ord('a')) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((shifted - ord('A')) % 26 + ord('A'))

    return encrypted_text

for char in text:
    letters.append(char)

frequency = {}

for letter in letters:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

most_common = max(frequency, key=frequency.get)
print(most_common)

#most common 10 letters in polish words
most_common_in_pl = ['a', 'i', 'o', 'e', 'z', 'n', 'r', 's', 'w', 'c']

for pl in most_common_in_pl:
    distance = ord(pl) - ord(most_common)
    print(caesar_cipher(text, distance))

    while True:
        choice = input("Has the text been decrypted? [y/n]: ")

        if choice.lower() == 'y' or choice.lower() == 'n':
            break
        else:
            print("Please enter a valid value")

    if choice.lower() == 'y':
        print("\033[91m" + caesar_cipher(text, distance) + "\033[0m")
        break