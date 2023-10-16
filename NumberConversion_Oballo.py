# Trisha Joy Oballo CS132G01
# Number Converter

# Functions
def decimal_to_binary(number):
    return bin(number)[2:]

def decimal_to_octal(number):
    return oct(number)

def decimal_to_hexa(number):
    return hex(number)

def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def binary_to_octal(binary_str):
    # Ensure the length of the binary string is a multiple of 3 by adding leading zeros
    while len(binary_str) % 3 != 0:
        binary_str = '0' + binary_str
    # Initialize variables
    octal_str = ''
    index = 0
    # Convert binary to octal in groups of 3 bits
    while index < len(binary_str):
        group = binary_str[index:index + 3]
        octal_digit = int(group, 2)
        octal_str += str(octal_digit)
        index += 3

    return octal_str

def binary_to_hexadecimal(binary_str):
    # convert binary to int
    num = int(binary_str, 2)
    # convert int to hexadecimal
    hex_num = hex(num)
    return (hex_num)

def octal_to_decimal(octal_str):
    return int(octal_str, 8)

def octal_to_binary(octal_str):
    decimal_number = int(octal_str, 8)
    binary_str = bin(decimal_number)[2:]
    return binary_str

def octal_to_hexadecimal(octal_str):
    decimal_number = int(octal_str, 8)
    hexadecimal_str = hex(decimal_number)[2:]
    return hexadecimal_str

def hexa_to_decimal(hexadecimal_str):
    return int(hexadecimal_str, 16)

def hexa_to_binary(hexadecimal_str):
    decimal_number = int(hexadecimal_str, 16)
    binary_str = bin(decimal_number)[2:]
    return binary_str

def hexa_to_octal(hexadecimal_str):
    decimal_number = int(hexadecimal_str, 16)
    octal_str = oct(decimal_number)[2:]
    return octal_str


# GREETINGS
print("Welcome, User!")
print("Please choose and input a number what you want to convert. ")
while True:
    # Decimal Converter
    print("-----Decimal Converter-----")
    print("1. Decimal to Binary"
          "\n2. Decimal to Octal"
          "\n3. Decimal to Hexadecimal")
    # Binary Converter
    print("-----Binary Converter-----")
    print("4. Binary to Decimal"
          "\n5. Binary to Octal"
          "\n6. Binary to Hexadecimal")
    # Octal Converter
    print("-----Octal Converter-----")
    print("7. Octal to Decimal"
          "\n8. Octal to Binary"
          "\n9. Octal to Hexadecimal")
    # Hexadecimal Converter
    print("-----Hexadecimal Converter-----")
    print("10. Hexadecimal to Decimal"
          "\n11. Hexadecimal to Binary"
          "\n12. Hexadecimal to Octal")
    # Exit
    print("--------------------------")
    print("13. Exit")

    # User Input
    choice = input("Enter your choice: ")

    if choice == '13':
        print("Goodbye, Thank you!")
        break

    if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
                      , '11', '12', '13']:
        print("Invalid choice. Please select a valid option.")
        continue

    user_input = input("Enter a number: ")

    # Result
    if choice == '1': # Decimal to Binary
        decimal_number = int(user_input)
        result = decimal_to_binary(decimal_number)
        print(f"Decimal to Binary: {result}")

    elif choice == '2': # Decimal to Octal
        decimal_number = int(user_input)
        result = decimal_to_octal(decimal_number)
        print(f"Decimal to Octal: {result}")

    elif choice == '3': # Decimal to Hexadecimal
        decimal_number = int(user_input)
        result = decimal_to_hexa(decimal_number)
        print(f"Decimal to Hexadecimal: {result}")

    elif choice == '4': # Binary to Decimal
        binary_str = user_input
        result = binary_to_decimal(binary_str)
        print(f"Binary to Decimal: {result}")

    elif choice == '5': # Binary to Octal
        binary_str = user_input
        result = binary_to_octal(binary_str)
        print(f"Binary to Octal: {result}")

    elif choice == '6':  # Binary to Hexadecimal
        binary_str = user_input
        result = binary_to_hexadecimal(binary_str)
        print(f"Binary to Hexadecimal: {result}")

    elif choice == '7':  # Octal to Decimal
        octal_str = user_input
        result = octal_to_decimal(octal_str)
        print(f"Octal to Decimal: {result}")

    elif choice == '8':  # Octal to Binary
        octal_str = user_input
        result = octal_to_binary(octal_str)
        print(f"Octal to Binary: {result}")

    elif choice == '9':  # Octal to Hexadecimal
        octal_str = user_input
        result = octal_to_hexadecimal(octal_str)
        print(f"Octal to Hexadecimal: {result}")

    elif choice == '10':  # Hexadecimal to Decimal
        hexadecimal_str = user_input
        result = hexa_to_decimal(hexadecimal_str)
        print(f"Hexadecimal to Decimal: {result}")

    elif choice == '11':  # Hexadecimal to Binary
        hexadecimal_str = user_input
        result = hexa_to_binary(hexadecimal_str)
        print(f"Hexadecimal to Binary: {result}")

    elif choice == '12':  # Hexadecimal to Octal
        hexadecimal_str = user_input
        result = hexa_to_octal(hexadecimal_str)
        print(f"Hexadecimal to Octal: {result}")
