# Project 1 - Cryptography
# Permutation cipher (student ID 161462, 161462 mod 3 = 2)
#
# How it works:
# The text is split into blocks of 6 letters. In each block the order
# of letters is changed according to the fixed permutation PERM.
# If the last block is too short, 'X' letters are added at the end.

# Permutation (hardcoded). Position i of the ciphertext gets the letter
# from position PERM[i] of the plaintext (counting from 0).
PERM = [2, 0, 4, 1, 5, 3]
PADDING = "X"


def check_permutation(perm):
    """Checks if the permutation is valid (at least 6 elements, numbers 0..n-1 without repeats)."""
    if len(perm) < 6:
        raise ValueError("Permutation must have at least 6 elements.")
    if sorted(perm) != list(range(len(perm))):
        raise ValueError("Permutation must contain numbers from 0 to " + str(len(perm) - 1) + " without repeats.")


def prepare_text(text):
    """Removes spaces, changes to uppercase and checks if there are only letters A-Z."""
    text = text.replace(" ", "").upper()
    if text == "":
        raise ValueError("Text cannot be empty.")
    for char in text:
        if char < "A" or char > "Z":
            raise ValueError("Invalid character: '" + char + "'. Only letters A-Z and spaces are allowed.")
    return text


def encrypt(text):
    n = len(PERM)
    # fill the text up to full blocks
    while len(text) % n != 0:
        text += PADDING

    result = ""
    for start in range(0, len(text), n):
        block = text[start:start + n]
        for i in range(n):
            result += block[PERM[i]]
    return result


def decrypt(ciphertext):
    n = len(PERM)
    if len(ciphertext) % n != 0:
        raise ValueError("Ciphertext length must be a multiple of " + str(n) + " (it is " + str(len(ciphertext)) + ").")

    result = ""
    for start in range(0, len(ciphertext), n):
        block = ciphertext[start:start + n]
        plain = [""] * n
        # reverse the permutation: letter from position i goes back to position PERM[i]
        for i in range(n):
            plain[PERM[i]] = block[i]
        result += "".join(plain)

    # remove padding from the end
    # (note: if the plaintext itself ended with X, it will be removed too)
    return result.rstrip(PADDING)


def menu():
    print("\n")
    print("MENU\n==========")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Show permutation")
    print("0. Exit")
    return input("Choose an option: ").strip()


def main():
    try:
        check_permutation(PERM)
    except ValueError as e:
        print("Permutation error:", e)
        return

    while True:
        try:
            choice = menu()

            if choice == "1":
                text = prepare_text(input("Enter plaintext: "))
                print("Ciphertext:", encrypt(text))

            elif choice == "2":
                text = prepare_text(input("Enter ciphertext: "))
                print("Plaintext:", decrypt(text))

            elif choice == "3":
                print("Permutation:", PERM)

            elif choice == "0":
                print("Goodbye")
                break

            else:
                print("There is no such option. Choose 0, 1, 2 or 3.")

        except ValueError as e:
            print("Error:", e)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye.")
            break


if __name__ == "__main__":
    main()
