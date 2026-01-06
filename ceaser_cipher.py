import os
def display_welcome():
    print(" ")
    print("Welcome to the Caesar Cipher")
    print("\n This program encrypts and decrypts text using Caesar Cipher.")
    print(" ")

def decrypt():
    '''
    so when the user enters somethinglike 'z' just adding the shift value to it i.e 122(z) + 3(shift value) 
    it doesnot give an alphabet it rather gives '{' which is not what I want. So in order to fix this, I first
    converted the letter into an alphabet number/index then '%26' makes sure that the value that is shifted
    stays around tha alphabet. So basically, z + 3 gives c. 
    '''
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

def process_file(filename, conv_mode):
    shift = int(input("Shift by how much : "))
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
                else:
                    converted_line += ch  
                    
                if letter_to_number >= 65 and letter_to_number <= 90:
                    base = 65
                    setter = letter_to_number - base 
                    
                    if conv_mode == 'e':
                        setter = (setter + shift) % 26
                    elif conv_mode == 'd':
                        setter = (setter - shift ) %26
            
            converted.append(converted_line)  
        
        for line in converted:
            print(line, end="")
    
def write_messages(text:str):
    with open("result.txt", "a") as file:
        for lines in text:
            file.write(f"{lines}")

write_messages("test 1,will this work?")

def is_file():
    path = input("Enter filename : ")
    if os.path.isfile(path):
        return True
    else:
        return False

def message_or_file():
    while True:
        choice = input("\nWould you like to encrypt(e), decrypt(d), or exit(x)? : ").lower()
        
        if choice == 'x':
            print("TATA, BYE BYE")
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

def main():
    display_welcome()
    enter_message()
