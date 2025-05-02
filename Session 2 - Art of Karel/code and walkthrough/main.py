from karel.stanfordkarel import *


#Main function:
   # The first thing that Karel needs to do before it picks up the beepers
   # move (pre condition - 1,1 facing East ; post condition - 1,2 facing East)
   # spread_beepers

def main():
    move()
    spread_beepers()
 
    pass

# Spread Beepers: 
     # How long do you keep going? 
     # while beeper is present: 
        # pick, move_to_empty_spot, put, return_to_pile
def spread_beepers():
    while beepers_present():
            pick_beeper()
            if beepers_present():
                move_to_empty_spot()
                put_beeper()
                return_to_pile()
    put_beeper()
    #we need to get karel go back home (1,1)
    go_home()
# Helper function: 
  # move_to_empty_spot:
    # pre condition - Karel is facing East, standing at 1,2 position
    # post condition - ??? Where Exactly should Karel end up? 1,3 
    
    # while beeper is present: 
         # move 
def move_to_empty_spot():
    while beepers_present():
        move()

# Helper function: 
  # return_to_pile:
    # pre condition - Karel is facing east, at 1,3
    # post condition - at 1,2 facing East
    # turn around, move to the wall, turn around, move

def return_to_pile():
    turn_around()
    move_to_the_wall()
    turn_around()
    move()

# Helper function:
  # go back home: 
    # turn around, move, turn around

def go_home():
    turn_around()
    move()
    turn_around()
# Helper function:
  #turn around: 
    # turn left twice

def turn_around():
    turn_left()
    turn_left()

# Helper function: 
  # move to the wall:
    # while front is clear, move
def move_to_the_wall():
    while front_is_clear():
        move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()