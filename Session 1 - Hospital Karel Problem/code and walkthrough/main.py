
from karel.stanfordkarel import *
"""
Program: Hospital Karel
Karel traverses 1st Street from west to east, building hospitals
wherever it encounters a beeper.
"""
def main():
    # Check the first position before starting to move
    if beepers_present():
        build_hospital()
    
    # Move along the first row, checking each position
    while front_is_clear():
        move()
        if beepers_present():
            build_hospital()

def build_hospital():
    """
    Karel picks up supplies and builds a hospital.
    Pre-condition: Karel is on a beeper, representing a
        pile of supplies. Karel is facing east.
    Post-condition: Karel is standing at the bottom
        of the last column of the hospital, facing east.
    """
    # pick up supplies
    pick_beeper()
    
    # Build first column upward
    turn_left()  # Face north
    put_three_beepers()
    
    # Move to top of second column
    turn_right()  # Face east
    move()
    
    # Build second column downward
    turn_right()  # Face south
    put_three_beepers()
    
    # Already at the bottom of second column, facing south
    turn_left()  # Face east for the next hospital

def put_three_beepers():
    """
    Karel places three beepers in a row.
    Pre-condition: Karel is on the corner where we want
        to place the first beeper.
    Post-condition: Karel is on the corner where it
        placed the third beeper in a row.
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()

def turn_right():
    """Turn Karel 90 degrees to the right"""
    turn_left()
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()