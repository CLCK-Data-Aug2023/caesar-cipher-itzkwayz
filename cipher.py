alphabet = "abcdefghijklmnopqrstuvwxyz"
encrypted_message= ""

message = input("Enter your secret message:").lower() #print(message)
shift = 5

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + shift) % 26
        new_character = alphabet[new_position]
        encrypted_message += new_character
    else:
        encrypted_message += character
print("Your encrypted message is " + encrypted_message) #print(encrypted message)