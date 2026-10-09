import cv2
import turtle
import time


IMAGE = "spiderman.png"

HEIGHT = 700

# Drawing speed
UPDATE_EVERY = 5
DELAY = 0.015

# Ignore very tiny contours
MIN_AREA = 30

# Simplify contour lines
APPROXIMATION = 1.2

print("Spider-Man Contour Tracer")
print("Project initialized successfully.")



# LOAD IMAGE


img = cv2.imread(IMAGE)

if img is None:
    print("=" * 50)
    print("ERROR: spiderman.png was not found.")
    print("Make sure spiderman.png is in the")
    print("same folder as spiderman.py.")
    print("=" * 50)
    exit()

print("Spider-Man image loaded successfully!")



# RESIZE IMAGE


ratio = HEIGHT / img.shape[0]

width = int(img.shape[1] * ratio)

img = cv2.resize(
    img,
    (width, HEIGHT)
)


# GRAYSCALE

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

# EDGE DETECTION

edges = cv2.Canny(
    gray,
    50,
    150
)

# FIND CONTOURS

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)

print("Contours detected:", len(contours))

# FILTER + SIMPLIFY CONTOURS

clean_contours = []

for contour in contours:

    area = cv2.contourArea(contour)

    if area > MIN_AREA:

        # Reduce excessive points
        simplified = cv2.approxPolyDP(
            contour,
            APPROXIMATION,
            False
        )

        if len(simplified) > 2:
            clean_contours.append(simplified)


# SORT CONTOURS

clean_contours = sorted(
    clean_contours,
    key=cv2.contourArea,
    reverse=True
)

print("Useful contours:", len(clean_contours))

# TURTLE WINDOW

screen = turtle.Screen()

screen.setup(
    width=img.shape[1] + 100,
    height=img.shape[0] + 100
)

screen.bgcolor("white")

screen.tracer(0, 0)


# TURTLE PEN

pen = turtle.Turtle()

pen.hideturtle()

pen.speed(0)

pen.pensize(1)

pen.color("black")

# COORDINATE CONVERSION

def map_point(point):

    x, y = point

    x = x - img.shape[1] / 2

    y = img.shape[0] / 2 - y

    return x, y

# DRAW AND FILL IMAGE

point_counter = 0

for contour in clean_contours:

    points = contour.reshape(-1, 2)

    if len(points) < 3:
        continue

    # Move to the starting point
    first_x, first_y = map_point(points[0])

    pen.penup()
    pen.goto(first_x, first_y)

    # Start filling this contour
    pen.begin_fill()

    pen.pendown()

    for px, py in points[1:]:

        x, y = map_point((px, py))

        pen.goto(x, y)

        point_counter += 1

        if point_counter % UPDATE_EVERY == 0:

            screen.update()

            time.sleep(DELAY)

    # Finish the filled contour
    pen.goto(first_x, first_y)

    pen.end_fill()

    pen.penup()

# FINISH

screen.update()

print("Drawing completed!")

turtle.done()