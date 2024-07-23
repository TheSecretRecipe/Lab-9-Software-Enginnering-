def encode(number):
    encoded_number = ''
    for char in number:
        encoded_number += str((int(char) + 3) % 10)
        return encoded_number


def decode(number):
    decoded_number = ''
    for char in number:
        decoded_number += str((int(char) - 3) % 10)
        return decoded_number


def main():
    stored_number = ''
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            number = input("Please enter the password to encode: ")
            stored_number = encode(number)
            print("Your password has been encoded and stored!")

        elif option == '2':
            if stored_number:
                original_number = decode(stored_number)
                print(f"The encoded password is {stored_number}, and the original password is {original_number}.")
            else:
                print("No encoded password stored yet. Please encode a password first.")

        elif option == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
