alphabet = "abcdefghijklmnopqrstuvwxyz"
encrpyted_message= ""

message = input("Enter your secret message:").lower() #print(message)
shift = 5

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + shift) % 26
        new_character = alphabet[new_position]
        encrpyted_message += new_character
    else:
        encrpyted_message += character
print("Your encrpyted message is " + encrpyted_message) #print(encrpyted message)