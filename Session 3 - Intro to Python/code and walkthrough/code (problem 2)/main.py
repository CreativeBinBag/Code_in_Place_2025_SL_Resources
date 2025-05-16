"""
Prompts the user for a weight on Earth
and prints the equivalent weight on different planets.
"""

def main():
    # Fill this function out!

    # Get the input from the user
    planet_choice = input("Enter your planet choice: ")

    # Gravity factors - constant
    MARS_GRAVITY = 0.378
    MERCURY_GRAVITY = 0.376 
    VENUS_GRAVITY = 0.889
    JUPITER_GRAVITY = 2.36

    # Get the input from the user
    earth_weight_str = input("Enter your earth weight: ")

    # Turn the string into float 
    earth_weight = float(earth_weight_str)
    
    # Initialize final_weight
    final_weight = 0.0 
    
    if planet_choice == "Mars":
        final_weight = MARS_GRAVITY * earth_weight
    if planet_choice == "Mercury":
        final_weight = MERCURY_GRAVITY * earth_weight
    if planet_choice == "Venus":
        final_weight = VENUS_GRAVITY * earth_weight
    if planet_choice == "Jupiter":
        final_weight = JUPITER_GRAVITY * earth_weight
  
    final_weight_rounded = round(final_weight, 2)
    
    # Print
    print("Your weight on " + planet_choice + "  is " + str(final_weight)) 

    pass

if __name__ == "__main__":
    main()