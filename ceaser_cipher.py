import os

def display_welcome():
    print(" ")
    print("Welcome to the Caesar Cipher")
    print("\n This program encrypts and decrypts text using Caesar Cipher.")
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
            setter = (setter - shift) % 26
            decrypted_text.append(chr(base + setter))
        else:
            decrypted_text.append(ch)
    
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
            setter = (setter + shift) % 26
            encrypted_text.append(chr(base + setter))
        else:
            encrypted_text.append(ch)
    
    for ch in encrypted_text:
        print(ch.upper(), end="")
    print("\n")
    
def is_file(filename):
    '''
    This function is not called anywhere because I have already setup a error handling 
    in teh process_file function.
    '''
    if os.path.isfile(filename):
        return True
    else:
        return False

def process_file(filename, conv_mode):
    shift = int(input("Shift by how much : "))
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            converted = []
            
            for line in lines:
                converted_line = ""  
                for ch in line:
                    letter_to_number = ord(ch)
                    
                    if letter_to_number >= 97 and letter_to_number <= 122:
                        base = 97
                        setter = letter_to_number - base
                        
                        if conv_mode == 'e':
                            setter = (setter + shift) % 26  
                        elif conv_mode == 'd':
                            setter = (setter - shift) % 26 
                        
                        converted_line += chr(base + setter)
                    
                    elif letter_to_number >= 65 and letter_to_number <= 90:
                        base = 65
                        setter = letter_to_number - base 
                        
                        if conv_mode == 'e':
                            setter = (setter + shift) % 26
                        elif conv_mode == 'd':
                            setter = (setter - shift) % 26
                        
                        converted_line += chr(base + setter)
                    
                    else:
                        converted_line += ch
                
                converted.append(converted_line)  
            
            for line in converted:
                print(line, end="")
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.\n")

def write_messsages(text):
    '''
    This function is not called anywhere
    '''
    with open("result.txt", "a") as file:
        for lines in text:
            file.write(lines)

def message_or_file():
    while True:
        choice = input("\nWould you like to encrypt(e), decrypt(d), or exit(x)? : ").lower()
        
        if choice == 'x':
            print("Thanks for using!")
            break
        
        elif choice == 'e':
            file_or_msg = input("Read from file(f) or console(c)? : ").lower()
            if file_or_msg == 'f':
                f_name = input("Enter file name: ")
                process_file(f_name, choice)
            elif file_or_msg == 'c':
                encrypt()
            else:
                print("Invalid choice. Please enter 'f' or 'c'.")
        
        elif choice == 'd':
            file_or_msg = input("Read from file(f) or console(c)? : ").lower()
            if file_or_msg == 'f':
                f_name = input("Enter file name: ")
                process_file(f_name, choice)
            elif file_or_msg == 'c':
                decrypt()
            else:
                print("Invalid choice. Please enter 'f' or 'c'.")
        
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'x'.")

display_welcome()
message_or_file()
