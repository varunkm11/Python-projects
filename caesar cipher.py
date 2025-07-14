def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)


# User input
print("=== Caesar Cipher Tool ===")
choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
text = input("Enter the message: ")
shift = int(input("Enter the shift value (number): "))

if choice == 'e':
    result = caesar_cipher_encrypt(text, shift)
    print("Encrypted Message:", result)
elif choice == 'd':
    result = caesar_cipher_decrypt(text, shift)
    print("Decrypted Message:", result)
else:
    print("Invalid choice! Please enter 'e' or 'd'.")
