def main():

    def encoder(password):
        # Encoded by Shiner
        encoded_password = ""
        for digit in password:
            # Converts the character to an integer, adds 3 from each, and appends to an empty string
            encoded_digit = str(int(digit) + 3)
            encoded_password += encoded_digit
        return encoded_password

    def menu():
        print('''Menu
    1. Encode
    2. Decode
    3. Exit''')

    while True:
        menu()
        option = int(input('Choose an option: '))
        if option == 1:
            user_input = input('Please enter a password to encode: ')
            result = encoder(user_input)
            print(result)
        if option == 2:
            user_input = int(input('Please enter a password to encode: '))
            result = decoder(user_input)
        if option == 3:
            exit()

if __name__ == '__main__':
    main()