# Coding Problems Solution

This project contains solutions to four coding problems:

1. Caesar Cipher encoding and decoding
2. Indian Currency Format conversion
3. Combining Lists with position and values
4. Minimizing Loss problem

## Problem 1: Caesar Cipher

A simple implementation of the Caesar cipher encryption technique where each letter is shifted by a specified number of positions.

### Usage

```python
from caesar_cipher import caesar_encode, caesar_decode

# Encoding a message
message = "Hello, World!"
shift = 3
encoded = caesar_encode(message, shift)
print(encoded)  # Output: "Khoor, Zruog!"

# Decoding a message
decoded = caesar_decode(encoded, shift)
print(decoded)  # Output: "Hello, World!"
```

## Problem 2: Indian Currency Format

Converts a floating-point number to the Indian numbering system format with appropriate comma separators.

### Usage

```python
from indian_currency import format_indian_currency

num = 123456.7891
formatted = format_indian_currency(num)
print(formatted)  # Output: "1,23,456.7891"
```

## Problem 3: Combining Lists

Combines two lists of elements with position and values, merging elements if more than half of one element is contained within the other.

### Usage

```python
from combine_lists import combine_lists

list1 = [
    {"positions": [10, 30], "values": ["value1", "value2"]},
    {"positions": [50, 70], "values": ["value5", "value6"]}
]

list2 = [
    {"positions": [15, 40], "values": ["value3", "value4"]},
    {"positions": [80, 100], "values": ["value7", "value8"]}
]

combined = combine_lists(list1, list2)
print(combined)
```

## Problem 4: Minimizing Loss

Finds the minimum loss when buying and selling a house across different years, with the constraint that the sale must be at a loss.

### Usage

```python
from minimize_loss import minimize_loss, minimize_loss_optimized

prices = [20, 15, 7, 2, 13]

# Using brute force approach
buy_year, sell_year, loss = minimize_loss(prices)
print(f"Buy in year {buy_year}, sell in year {sell_year}, with loss {loss}")

# Using optimized approach
buy_year, sell_year, loss = minimize_loss_optimized(prices)
print(f"Buy in year {buy_year}, sell in year {sell_year}, with loss {loss}")
```

## Running the Examples

Each Python file contains an example usage section that can be executed directly:

```bash
python caesar_cipher.py
python indian_currency.py
python combine_lists.py
python minimize_loss.py
``` 