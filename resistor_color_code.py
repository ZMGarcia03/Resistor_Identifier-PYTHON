# Dictionary to map color to digit or multiplier
COLOR_CODES = {
    "black": (0, 1),
    "brown": (1, 10),
    "red": (2, 100),
    "orange": (3, 1000),
    "yellow": (4, 10000),
    "green": (5, 100000),
    "blue": (6, 1000000),
    "violet": (7, 10000000),
    "gray": (8, 100000000),
    "white": (9, 1000000000),
    "gold": (-1, 0.1),
    "silver": (-2, 0.01)
}

def calculate_resistance(band1, band2, multiplier_band):
    """
    Calculate the resistance value based on color bands.

    Parameters:
    band1 (str): The color of the first band.
    band2 (str): The color of the second band.
    multiplier_band (str): The color of the multiplier band.

    Returns:
    float: The resistance value in ohms.
    """
    if band1 not in COLOR_CODES or band2 not in COLOR_CODES or multiplier_band not in COLOR_CODES:
        raise ValueError("Invalid color band. Please use valid resistor colors.")

    first_digit = COLOR_CODES[band1][0]
    second_digit = COLOR_CODES[band2][0]
    multiplier = COLOR_CODES[multiplier_band][1]

    resistance_value = (first_digit * 10 + second_digit) * multiplier
    return resistance_value

def main():
    print("Resistor Color Code Calculator")
    print("Enter the color of the bands:")
    try:
        band1 = input("First band: ").lower()
        band2 = input("Second band: ").lower()
        multiplier_band = input("Multiplier band: ").lower()

        resistance = calculate_resistance(band1, band2, multiplier_band)
        print(f"The resistance value is: {resistance:.2f} ohms")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
