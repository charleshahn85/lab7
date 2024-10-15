#CIS-12 Lab 7

import string

alphabet = string.ascii_uppercase
encrypted_texts = []

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)


def index_to_letter(index, alphabet):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)
    return (key_index + plaintext_index) % len(alphabet)


def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    return (cipher_index - key_index) % len(alphabet)


def encrypt_vigenere(key, plaintext, alphabet):
    key = key.upper()
    plaintext = plaintext.upper()
    cipher_text = []
    for i, char in enumerate(plaintext):
        if char in alphabet:
            key_char = key[i % len(key)]
            cipher_index = vigenere_index(key_char, char, alphabet)
            cipher_text.append(index_to_letter(cipher_index, alphabet))
        else:
            cipher_text.append(char)
    return ''.join(cipher_text)


def decrypt_vigenere(key, cipher_text, alphabet):
    key = key.upper()
    plain_text = []
    for i, char in enumerate(cipher_text):
        if char in alphabet:
            key_char = key[i % len(key)]
            plain_index = undo_vigenere_index(key_char, char, alphabet)
            plain_text.append(index_to_letter(plain_index, alphabet))
        else:
            plain_text.append(char)
    return ''.join(plain_text)


def encrypt():
    plaintext = input("Enter the plaintext to encrypt: ").upper()
    key = input("Enter the encryption key: ").upper()
    cipher_text = encrypt_vigenere(key, plaintext, alphabet)
    encrypted_texts.append((key, cipher_text))
    print("Text encrypted and stored.")


def decrypt():
    if not encrypted_texts:
        print("No encrypted texts to decrypt.")
        return

    print("Encrypted texts:")
    for i, (key, text) in enumerate(encrypted_texts):
        print(f"{i + 1}. {text[:20]}..." if len(text) > 20 else f"{i + 1}. {text}")

    try:
        choice = int(input("Enter the number of the text you want to decrypt: ")) - 1
        if 0 <= choice < len(encrypted_texts):
            key, cipher_text = encrypted_texts[choice]
            plain_text = decrypt_vigenere(key, cipher_text, alphabet)
            print(f"Decrypted text: {plain_text}")
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def dump_encrypted():
    if not encrypted_texts:
        print("No encrypted texts to display.")
    else:
        for i, (key, text) in enumerate(encrypted_texts):
            print(f"Encrypted text {i + 1}: {text}")
            print(f"Key: {key}\n")


def quit_program():
    print("CYA!")
    exit()


menu_options = [
    ["1. Encrypt", encrypt],
    ["2. Decrypt", decrypt],
    ["3. Dump Encrypted Text", dump_encrypted],
    ["4. Quit", quit_program]
]


def main():
    while True:
        print("\nVigenère Cipher Menu:")
        for option in menu_options:
            print(option[0])
        choice = input("Enter your choice (1-4): ")
        for option in menu_options:
            if choice == option[0][0]:
                option[1]()
                break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()