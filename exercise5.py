# Breaking Caesar’s Cipher
# For this exercise, I studied the CSP Python online interactive textbook.
# I believe to make the computer choose the right decryption, a dictionary
# should be implemented. I could not go that far since I just started learning how to code.

def break_cipher(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        #else:
            #result = result + letter

    return result


def main():
    text = input("Give me the Caesar's Cipher!: ")

    for key in range(1, 27):
        decrypted = break_cipher(key, text)
        print(key, decrypted, sep=". ")

    text2 = input("Which one is correct? Enter only the number: ")
    real_key = int(text2)
    real_decrypted = break_cipher(real_key, text)
    print(real_decrypted)


if __name__ == "__main__":
    main()
