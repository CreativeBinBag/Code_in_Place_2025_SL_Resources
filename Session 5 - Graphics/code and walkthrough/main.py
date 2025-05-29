from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
    print('Random Circles')
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    num_of_random_circles = random.randint(5, N_CIRCLES)
    for i in range(num_of_random_circles):
        draw_random_circle(canvas)
    
def random_color():
    """
    This is a function to use to get a random color for each circle. We have
    defined this for you and there is no need to edit code in this function,
    but feel free to read it over if you are interested. 
    """
    colors = ['blue', 'purple', 'salmon', 'lightblue', 'cyan', 'forestgreen']
    return random.choice(colors)

# Function draw_random_circle
   # How do we randomly get a color? random_color()
   # What information do we need for the create_oval() function? x1, y1, x2, y2
 
def draw_random_circle(canvas):
    color = random_color()
    circle_size_random = random.randint(10, 50)
    x1 = random.randint(0, CANVAS_WIDTH - circle_size_random )
    y1 = random.randint(0, CANVAS_HEIGHT - circle_size_random )
    x2 = x1 + circle_size_random
    y2 = y1 + circle_size_random
    canvas.create_oval(x1,y1,x2,y2,color)


if __name__ == '__main__':
    main()