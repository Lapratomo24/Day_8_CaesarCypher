logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to Caesar Cipher!")
direction = input("Type 'encode' to encrypt or 'decode' to decrypt\n").lower()
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

# game logic

def encrypt(text_input, shift_num):
    encoded_text = ""
    
    for letter in text_input:
        position = alphabet.index(letter)
        new_position = position + shift_num
        new_letter = alphabet[new_position]
        encoded_text += new_letter
    print(f"The encoded text is {encoded_text}.")
        
encrypt(text, shift)

def decrypt(text_input, shift_amount):
    decoded_text = ""
    
    for letter in text_input:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    print(f"The decoded text is {decoded_text}.")

decrypt(text, shift)