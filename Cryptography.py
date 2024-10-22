import base64
import binascii
import codecs

# Encode Input
def encode_base64(data):
    return base64.b64encode(data.encode()).decode()

def decode_base64(data):
    return base64.b64decode(data).decode()

def encode_hex(data):
    return data.encode().hex()

def decode_hex(data):
    return bytes.fromhex(data).decode()

def encode_base85(data):
    return base64.b85encode(data.encode()).decode()

def decode_base85(data):
    return base64.b85decode(data).decode()

def encode_binary(data):
    return ''.join(format(ord(char), '08b') for char in data)

def decode_binary(data):
    binary_int = int(data, 2)
    return binary_int.to_bytes((binary_int.bit_length() + 7) // 8, 'big').decode()

def encode_rot13(data):
    return codecs.encode(data, 'rot_13')

def decode_rot13(data):
    return codecs.decode(data, 'rot_13')

# Hexdump Encoder/Decoder (Basic)
def encode_hexdump(data):
    return binascii.hexlify(data.encode()).decode()

def decode_hexdump(data):
    return binascii.unhexlify(data).decode()

# User Interface
def main():
    while True:
        print("\nCryptography Encoder/Decoder:")
        print("1. Base64")
        print("2. Hex")
        print("3. Base85")
        print("4. Binary")
        print("5. ROT13")
        print("6. Hexdump")
        print("7. Exit")

        choice = input("\nSelect an option (1-7): ")

        if choice == '7':
            print("Exiting...")
            break

        input_data = input("Enter the data: ")

        if choice == '1':
            print("\nBase64 Encoded:", encode_base64(input_data))
            print("Base64 Decoded:", decode_base64(encode_base64(input_data)))
        elif choice == '2':
            print("\nHex Encoded:", encode_hex(input_data))
            print("Hex Decoded:", decode_hex(encode_hex(input_data)))
        elif choice == '3':
            print("\nBase85 Encoded:", encode_base85(input_data))
            print("Base85 Decoded:", decode_base85(encode_base85(input_data)))
        elif choice == '4':
            print("\nBinary Encoded:", encode_binary(input_data))
            print("Binary Decoded:", decode_binary(encode_binary(input_data)))
        elif choice == '5':
            print("\nROT13 Encoded:", encode_rot13(input_data))
            print("ROT13 Decoded:", decode_rot13(encode_rot13(input_data)))
        elif choice == '6':
            print("\nHexdump Encoded:", encode_hexdump(input_data))
            print("Hexdump Decoded:", decode_hexdump(encode_hexdump(input_data)))
        else:
            print("Invalid option! Please choose a valid number.")

if __name__ == '__main__':
    main()
