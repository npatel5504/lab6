
# decoded by mae lea gordon
def encode(password):
    #12345678
    encoded_password = ""
    for num in password:
        int_num = int(num) #turn each element into an integer
        encoded_int_num = int_num + 3 #add 3 to each element
        new_encoded_int_num = encoded_int_num % 10 # 8 --> 11 ... 11%10 = 1 (avoids negative numbers, sticks to a 0-9 range)
        encoded_string_num = str(new_encoded_int_num) #turn each element back to a string
        encoded_password += encoded_string_num #add to empty string
        continue
    return encoded_password


def decode(encoded_password):
    res = ""
    for num in encoded_password:
        minus_3 = int(num) - 3
        more_than_10 = minus_3 % 10
        res += str(minus_3)
    return res



def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    program = True
    while True:
        option = int(input("Please enter an option: ")) #menu option
        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encode(password) #stores encoded_password into a variable so the decode function can take it in
            print()
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is", encoded_password, ", and the original password is", password, end=".")
            print()
            print()
        elif option == 3:
            program = False
            break


if __name__ == "__main__":
    main()