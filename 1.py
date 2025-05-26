def convert_temperature(temp, unit):
    if unit.upper() == 'F':
        result = (temp - 32) * 5 / 9
    elif unit.upper() == 'C':
        result = (temp * 9 / 5) + 32
    else:
        raise ValueError("Invalid unit. Use 'F' for Fahrenheit or 'C' for Celsius.")
    return round(result, 2)

print(convert_temperature(100, 'C'))
print(convert_temperature(212, 'F'))
