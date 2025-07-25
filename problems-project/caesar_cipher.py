def caesar_encode(message, shift):
    """
    Encodes a message using Caesar cipher with specified shift.
    
    Args:
        message (str): The plaintext message to be encoded
        shift (int): The number of positions to shift each character
    
    Returns:
        str: The encoded message
    """
    encoded = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            # Apply shift and wrap around the alphabet (26 letters)
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded += encoded_char
        else:
            # Keep non-alphabetic characters as they are
            encoded += char
    return encoded

def caesar_decode(encoded_message, shift):
    """
    Decodes a message that was encoded using Caesar cipher.
    
    Args:
        encoded_message (str): The message to be decoded
        shift (int): The number of positions that were used to shift each character
    
    Returns:
        str: The decoded message
    """
    # Decoding is simply encoding with a negative shift
    return caesar_encode(encoded_message, -shift)

# Example usage
if __name__ == "__main__":
    message = "Hello, World!"
    shift = 3
    
    encoded = caesar_encode(message, shift)
    decoded = caesar_decode(encoded, shift)
    
    print(f"Original message: {message}")
    print(f"Encoded message: {encoded}")
    print(f"Decoded message: {decoded}") 