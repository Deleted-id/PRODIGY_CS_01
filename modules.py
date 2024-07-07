# encrypt text method
def encrypt_text(string, shift):
    encrypted_text = ""
    for s in string:
        if s.isalpha():
            ascii_offset = 65 if s.isupper() else 97
            encrypted_text += chr((ord(s) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += s
    return encrypted_text

# decrypt text method      
def decrypt_text(string, shift):
    return encrypt_text(string, -shift)