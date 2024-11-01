import math

plain_text = 'pawelspychalski'.upper()
key = 'key'.upper()

if len(plain_text) > len(key):
    key = key * round(len(plain_text)/len(key))
    key = key[:len(plain_text)]

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encrypted_text = ''

i = 0

for letter in plain_text:
    if alphabet.find(letter) + alphabet.find(key[i]) > len(alphabet) - 1:
        shift = (alphabet.find(letter) + alphabet.find(key[i])) - len(alphabet) - 1
    else:
        shift = alphabet.find(letter) + alphabet.find(key[i])

    i += 1
    encrypted_text += alphabet[shift]

print(encrypted_text)

i = 0

og_text = ''

for letter in encrypted_text:
    #print(letter)
    if alphabet.find(letter) - alphabet.find(key[i]) < 0:
        shift = alphabet.find(letter) - alphabet.find(key[i]) + len(alphabet) + 1
    else:
        shift = alphabet.find(letter) - alphabet.find(key[i])

    og_text += alphabet[shift]
    i+=1

print(og_text)




