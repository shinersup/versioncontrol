# Code by Shiner Supre
def main():
    def encode(password):
        encoded_password = ""
        for digit in password:
            # Converts the character to an integer, adds 3 from each, and appends to an empty string
            encoded_digit = str((int(digit) + 3) % 10)
            encoded_password += encoded_digit
        return encoded_password

    def decode(password):
        decoded_pass = []
        for i in list(password):
            decoded_pass.append(str((int(i)-3) % 10)) # Reverses encoding process
        return ''.join(decoded_pass)

    def menu():
        print('''Menu
-------------
1. Encode
2. Decode
3. Quit''')

    while True:
        menu()
        option = input('Please enter an option: ')
        if option not in ['1', '2', '3']:
            continue
        if option == '1':
            user_input = input('Please enter your password to encode: ')
            encoded_result = encode(user_input)
            print('Your password has been encoded and stored!')
        if option == '2':
            try: # checks if there is a password to decode
                decoded_result = decode(encoded_result)
                print(f'The encoded password is {encoded_result}, and the original password is {decoded_result}')
            except: 
                print('Please encode a password first.')
        if option == '3':
            exit()


if __name__ == '__main__':
    main()
