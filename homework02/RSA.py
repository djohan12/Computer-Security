def RSA_encrypt(plaintext):
    print("Problem4: ")
    ciphertext=[]
    for c in plaintext:
        ciphertext.append(((((ord(c)-65)**53)%77)**37)%77)
    print(f"RSA Encrypted Ciphertext: {' '.join(list(map(str,(ciphertext))))}")
    return ciphertext

def RSA_decrypt(cipher):
    plaintext=''
    for c in cipher:
        plaintext+=chr(((((c**13)%77)**17)%77)+65)
    print(f"RSA Decrypted Plaintest: {plaintext}")
    
def main():
    cipher = RSA_encrypt("BRIGHT")
    RSA_decrypt(cipher)
    
if __name__ == "__main__":
    main()