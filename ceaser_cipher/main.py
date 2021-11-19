# importing the module which contain logo
import art

# collection of characters for encryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ceaser function for encryption and decryption according to user directions
def caesar(plain_text, shift_amount, dirc):
    end_text = ""

    for i in plain_text:
        if i in alphabet:
            index = alphabet.index(i)
            if dirc == "encode":
                index = (index + shift_amount)%26
            else:
                index = index - shift_amount
            end_text += alphabet[index]
        else:
            end_text+= i
    print(f"Here's the {dirc}d result: {end_text}")

# printing logo
print(art.logo)

#setting a flag for repeating the game
flag = True

# repeating the game until the user quits
while flag:
    # taking encryption or decryption and plain text and the key for encryption
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text = text, shift_amount = shift%26, dirc = direction)

    # asking the user if he wishes to continue or not
    print("Type 'yes' if you want to go again. Otherwise type 'no'")
    result = input().lower()

    # setting flag to false when the user wishes to stop
    if result == 'no':
        flag = False


