import sys

def encode_Goodluck_to_file():
    if len(sys.argv) < 3:
        print("Please provide a filename as the first argument and the text to encode as the second argument.")
        return

    filename = sys.argv[1]
    text = sys.argv[2]
    Goodluck_code = ' 01 '  # začátek programu

    for char in text:
        char_value = ord(char)  # ASCII hodnota znaku
        # přičteme k hodnotě paměti
        Goodluck_code += ('01' * char_value) + ' '
        # vypíšeme hodnotu paměti jako ASCII znak
        Goodluck_code += '01' * 6 + ' '
        # resetujeme hodnotu paměti na 0
        Goodluck_code += '01 '

    Goodluck_code += '01'  # konec programu

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(Goodluck_code)
    print(f"Goodluck code saved to file '{filename}'.")

if __name__ == "__main__":
    encode_Goodluck_to_file()