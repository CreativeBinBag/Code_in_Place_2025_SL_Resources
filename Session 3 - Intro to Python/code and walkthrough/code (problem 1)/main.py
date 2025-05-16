"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

def main():

    # Constants
    MARS_GRAVITY_FACTOR = 0.378 # 37.8%

    # Get the input from the user
    earth_weight_str = input("Enter your earth weight: ")

    # Turn the string into float 
    earth_weight = float(earth_weight_str)
    
    # Calculate Mars weight
    mars_weight = earth_weight * MARS_GRAVITY_FACTOR

    # Rounding:
    rounded_mars_weight = round(mars_weight, 2)

    # Print
    print("Your weight on Mars is: " + str(rounded_mars_weight))

    pass

if __name__ == "__main__":
    main()