def display_welcome():
    print(" ")
    print("------Welcome to THE DECIPHER-er------")
    print(" ")

def decrypt():
    text = input("Enter text to decipher: ").lower()
    shift = int(input("Shift by how much: "))
    decrypted_text = []
    
    for ch in text:
        letter_to_number = ord(ch)
        if letter_to_number >= 97 and letter_to_number <= 122:
            base = 97
            setter = letter_to_number - base
            setter = setter - shift
            decrypted_text.append(chr(base + setter % 26))
        else:
            decrypted_text.append(ch)
    
    print("\nDecrypted: ", end="")
    for ch in decrypted_text:
        print(ch.upper(), end="")
    print("\n")

def encrypt():
    text = input("Enter text: ").lower()
    shift = int(input("Shift by how much: "))
    encrypted_text = []
    
    for ch in text:
        letter_to_number = ord(ch)
        if letter_to_number >= 97 and letter_to_number <= 122:
            base = 97
            setter = letter_to_number - base
            setter = setter + shift
            encrypted_text.append(chr(base + setter % 26))
        else:
            encrypted_text.append(ch)
    
    print("\nEncrypted: ", end="")
    for ch in encrypted_text:
        print(ch.upper(), end="")
    print("\n")

def enter_message():
    while True:
        conv_mode = input("Encrypt(e) or Decrypt(d) or exit to exit: ")
        
        if conv_mode == 'exit':
            print("Thanks for using this!")
            break
        elif conv_mode == 'e':
            encrypt()
        elif conv_mode == 'd':
            decrypt()
        else:
            print("Invalid mode\n")

def main():
    display_welcome()
    enter_message()
