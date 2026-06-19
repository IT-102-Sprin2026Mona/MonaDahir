#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" text using base64 encoding
# By Mona

"""
Base64 Encodes plaintext / Decoder
"""

#Imported library
import base64


"""
Encoding plaintext to Base64

Steps:
1.) Convert the string into UTF-8
2.) Pass the bytes into b64encode()
3.) Return the encoded string
"""

def encode_to_base64(plaintext: str) -> str:

    # Convert text to bytes
    text_as_bytes = plaintext.encode("utf-8")

    # Encode bytes back to string
    encoded_bytes = base64.b64encode(text_as_bytes)

    # Convert bytes back to string
    return encoded_bytes.decode("utf-8")

"""
Decoding Base64 back to plaintext

Steps:
1.) Convert Base64 string into bytes
2.) Decode Base64 bytes
3.) Convert decoded bytes back into UTF-8 string
"""

def decode_to_base64(encoded_text: str) -> str:

    # Convert Base64 string to bytes
    encoded_as_bytes = encoded_text.encode("utf-8")

    # Decode Base64 bytes
    decoded_bytes = base64.b64decode(encoded_as_bytes)

    # Convert decoded bytes back to string
    return decoded_bytes.decode("utf-8")

#Main function
def main():

    print("=== Base64 Encoder / Decoder ===")
    print("NOTE: Base64 is NOT encryption.\n")

    #User input
    message = input("Enter your message to encode: ").strip()

    # Check for empty input
    if not message:
        print("No message entered. Exiting.")
        return 
    # Encode message
    encoded = encode_to_base64(message)

    print("\nEncoded Base64:")
    print(encoded)

    # Decode message
    decoded = decode_to_base64(encoded)

    print("\nDecoded message:")
    print(decoded)

    #Validation
    if decoded == message:
        print("\nConfirmation: Decoded message matches original input.")
    else:
        print("\nError: Decoded message does not match original input.")


# Run the program
if __name__ == "__main__":
    main()


