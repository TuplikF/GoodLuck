import sys

def decode_Goodluck_from_file():
    if len(sys.argv) < 2:
        print("Please provide a filename as the first argument.")
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            Goodluck_code = file.read()
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
        return

    Goodluck_parts = Goodluck_code.split()
    text = ''

    if len(Goodluck_parts) < 3:
        raise ValueError('Invalid Goodluck code')

    if len(Goodluck_parts[0]) != 1 or len(Goodluck_parts[-1]) != 1:
        raise ValueError('Invalid Goodluck code: Missing header/footer')

    for i in range(2, len(Goodluck_parts) - 2, 3):
        if len(Goodluck_parts[i]) != 6:
            raise ValueError('Invalid Goodluck code: Missing print command')
        if len(Goodluck_parts[i+1]) != 1:
            raise ValueError('Invalid Goodluck code: Missing reset command')
        char_value = len(Goodluck_parts[i-1])
        text += chr(char_value)

    print(text)

if __name__ == "__main__":
    decode_Goodluck_from_file()