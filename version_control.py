def main():

    def encoder(password):
        # Encoded by Shiner
        encoded_password = ""
        for digit in password:
            # Converts the character to an integer, adds 3 from each, and appends to an empty string
            encoded_digit = str(int(digit) + 3)
            encoded_password += encoded_digit
        return encoded_password
    
    # Add decoder function here

    def menu():
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')

    while True:
        menu()
        option = int(input('Please enter an option: '))
        if option == 1:
            user_input = input('Please enter your password to encode: ')
            encoded_result = encoder(user_input)
            print('Your password has been encoded and stored!')
        if option == 2:
            user_input = encoded_result
            decoded_result = decoder(user_input)
            print(f'The encoded password is {encoded_result}, and the original password is {decoded_result}.')
        if option == 3:
            exit()

if __name__ == '__main__':
    main()