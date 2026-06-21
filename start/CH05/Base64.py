#!/usr/bin/env python3
# Script that "encrypts"/"decrypts" tex#t using base64 encoding 
# By Mona Dahir

"""
This script is to take an input and encode and decode BASE64
"""

#Imported libaries
import base64

"""
encoding plaintext to base64
we will do the following steps
1.) Convert the string using UTF-8
2.) Pass the bytes into a function called b64.encoded
4.) Resulted bytes in a returned
"""

def encode_to_base64(plaintext: str) -> str:
    text_to_bytes = plaintext.encoded("utf-8") # "Hello" -> b"Hello" == 0x48 0x65 0x6c
    encode_bytes = base64.b64encode(text_to_bytes) # b"Hello" -> b"SGVsbG8="
    return encode_bytes.decode("utf-8") # b"SGVsbG8=" -> "SGVsbG" 
    
