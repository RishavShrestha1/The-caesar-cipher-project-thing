def display_welcome():
    print(" ")
    print("------Welcome to THE DECIPHER-er------")
    

def decrypt():
    text = input("Enter text to decipher : ").lower()
    shift = int(input("Shift by how much : "))
    decrypted_text = [] 
                
    for ch in text:
        letter_to_number = ord(ch)
                    
        if letter_to_number >= 97 and letter_to_number <=122:
            base = 97
            setter = letter_to_number - base
            setter = setter - shift
            decrypted_text.append(chr(base + setter % 26))
                    
        else:
            decrypted_text.append(ch)
    
            for ch in decrypted_text:
                print(ch.upper, end = "")
            
def encrypt():
    text = input("Enter text : ").lower()
    shift = int(input("Shift by how much : "))
    encrypted_text = []
                
    for ch in text:
        '''
        so when the user enters somethinglike 'z' just adding the shift value to it i.e 122(z) + 3(shift value) 
        doesnot give an alphabet it rather gives '{' which is not what I want. So in order to fix this, I first
        converted the letter into an alphabet number/index then '%26' makes sure that the value that is shifted
        stays around tha alphabet. So basically, z + 3 gives c. 
        '''
                    
        letter_to_number = ord(ch)
                    
        if letter_to_number >= 97 and letter_to_number <=122:
            base = 97
            setter = letter_to_number - base
            setter = setter + shift
            encrypted_text.append(chr(base + setter % 26))
                    
        else:
            encrypted_text.append(ch)
                
    for ch in encrypted_text:
        print(ch.upper(), end="")

def enter_message():
    conv_mode = input("Encrypt(e) or Decrypt(d) or exit to exit : ")
    
    while True:
        if conv_mode == 'exit':
            print("THanks for using this ")
            break
        elif conv_mode == 'e':
            encrypt()
        elif conv_mode == 'd':
            decrypt()
        else:
            print("Invalid mode")
