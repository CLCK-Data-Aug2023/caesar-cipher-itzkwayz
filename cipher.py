alphabet = "abcdefghijklmnopqrstuvwxyz"
new_message= ""

message = input("Enter your secret message:").lower() #print(message)
shift = 5

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + shift) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character
print("Your new message is " + new_message)