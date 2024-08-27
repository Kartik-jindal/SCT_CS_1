letters = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(plaintext, key):
    ciphertext = ''
    for i in plaintext:
        i = i.lower()
        if i != ' ':
            index = letters.find(i)
            if index == -1:
                ciphertext += i
            else:
                new_index = (index + key) % 26
                ciphertext += letters[new_index]
        else:
            ciphertext += i
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    for i in ciphertext:
        i = i.lower()
        if i != ' ':
            index = letters.find(i)
            if index == -1:
                plaintext += i
            else:
                new_index = (index - key) % 26
                plaintext += letters[new_index]
        else:
            plaintext += i
    return plaintext

def main():
    action = input("E for Encryption or D for Decryption: ").lower()
    
    if action == "e":
        print("Encryption")
        key = int(input("Enter the key (from 1 to 26): "))
        text = input("Enter the text to encrypt: ")
        ciphertext = encrypt(text, key)
        print("Encrypted Text:", ciphertext)
    elif action == "d":
        print("Decryption")
        key = int(input("Enter the key (from 1 to 26): "))
        text = input("Enter the text to decrypt: ")
        plaintext = decrypt(text, key)
        print("Decrypted Text:", plaintext)
    else:
        print("Invalid choice. Please enter 'E' for Encryption or 'D' for Decryption.")

if __name__ == "__main__":
    main()
