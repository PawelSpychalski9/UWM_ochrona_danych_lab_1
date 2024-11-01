def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                encrypted_text += chr((shifted - ord('a')) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((shifted - ord('A')) % 26 + ord('A'))

    return encrypted_text

text = "PAWELSPYCHALSKI"
shift = 2
print(caesar_cipher(text, shift))

encrypted_text = caesar_cipher(text, shift)
shift = -2
print(caesar_cipher(encrypted_text, shift))