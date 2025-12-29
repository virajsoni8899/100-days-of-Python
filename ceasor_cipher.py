alphabets = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]

direaction = input("type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("type your message:\n").lower()
shift = int(input("type the shift number:\n"))


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            cipher_text += alphabets[shifted_position]
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

def decode(original_text, shift_amount):
    decoded_text = ""
    for letter in original_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter)-shift_amount
            shifted_position %= len(alphabets)
            decoded_text += alphabets[shifted_position]
        else:
            decoded_text += letter
    print(f"The decoded text is {decoded_text}")
        

def ceasor(original_text, shift_amount, direction):
    if direaction == "encode":
        encrypt(original_text=original_text, shift_amount=shift_amount)
    elif direaction == "decode":
        decode(original_text=original_text, shift_amount=shift_amount)
    else:
        print("Invalid direction")

ceasor(original_text=text, shift_amount=shift, direction=direaction)

    

