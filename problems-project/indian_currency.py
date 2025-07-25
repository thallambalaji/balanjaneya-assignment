def format_indian_currency(number):
    """
    Converts a floating point number to Indian currency format with commas.
    
    Args:
        number (float): The number to be formatted
    
    Returns:
        str: The formatted number in Indian currency format
    """
    # Convert the number to string and split into integer and decimal parts
    str_number = str(number)
    if '.' in str_number:
        integer_part, decimal_part = str_number.split('.')
    else:
        integer_part, decimal_part = str_number, ""
    
    # Handle the case when the integer part has 3 or fewer digits
    if len(integer_part) <= 3:
        result = integer_part
    else:
        # First group: Last 3 digits
        result = integer_part[-3:]
        remaining = integer_part[:-3]
        
        # Add commas after every 2 digits from right to left
        while remaining:
            if len(remaining) <= 2:
                result = remaining + "," + result
                break
            else:
                result = remaining[-2:] + "," + result
                remaining = remaining[:-2]
    
    # Append the decimal part if it exists
    if decimal_part:
        result += "." + decimal_part
    
    return result

# Example usage
if __name__ == "__main__":
    test_numbers = [
        123456.7891,
        1234567.89,
        12345,
        1234567890.12345,
        999
    ]
    
    for num in test_numbers:
        formatted = format_indian_currency(num)
        print(f"{num} -> {formatted}") 