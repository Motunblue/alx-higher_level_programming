#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(roman_string)):
            value = numerals[roman_string[i]]
            next_value = None
            if i + 1 < len(roman_string):
                next_value = numerals[roman_string[i + 1]]
            if next_value is not None and value < next_value:
                total -= value
            else:
                total += value
        return total
    else:
        return 0
