import math

while True:
    #key = input("Insert your key")
    key = 43215
    try:
        key = int(key)
        break

    except ValueError:
        print("Please enter a number")

key = str(key)
plain_text = "pawelspychalski"

no_of_columns = len(key)
no_of_rows =  math.ceil(len(plain_text)/no_of_columns)

print(no_of_columns, no_of_rows)

if len(plain_text) < no_of_columns * no_of_rows:
    plain_text = plain_text + ((no_of_columns*no_of_rows)-len(plain_text))*"-"

print(plain_text)

table = {}
for i in range(no_of_columns):
    for j in range(no_of_rows):
        if key[i] in table.keys():
            table[key[i]] += plain_text[j + i + j * (no_of_columns - 1)]

        else:
            table[key[i]] = plain_text[j + i]

sorted_table = {key: table[key] for key in sorted(table.keys())}

#print(sorted_table.values())
text = ''.join(sorted_table.values())
print(text)







