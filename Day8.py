# Ceasar cipher code challenge

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

print(logo)

alphabet = " abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift number:\n"))

def encrypt(original_text, shift_amt):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amt 
        shifted_position = shifted_position % len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")

def decrypt(original_text, shift_amt):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) -shift_amt
        shifted_position = shifted_position % len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the decoded result: {output_text}")

def caesar(direction, text, shift):
    if direction == "encode":
        encrypt(original_text=text, shift_amt=shift)
    else:
        decrypt(original_text=text, shift_amt=shift)

caesar(direction, text, shift)
