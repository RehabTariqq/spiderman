import cv2
import turtle


# ==========================================
# SETTINGS
# ==========================================

IMAGE = "spiderman.png"

HEIGHT = 700

UPDATE_EVERY = 3


# ==========================================
# LOAD IMAGE
# ==========================================

img = cv2.imread(IMAGE)


if img is None:

    print("=" * 50)
    print("ERROR: spiderman.png was not found.")
    print("=" * 50)
    print("Make sure spiderman.png is in the")
    print("same folder as spiderman.py.")
    print("=" * 50)

    exit()


print("Spider-Man image loaded successfully!")


# ==========================================
# RESIZE IMAGE
# ==========================================

ratio = HEIGHT / img.shape[0]

width = int(img.shape[1] * ratio)

img = cv2.resize(
    img,
    (width, HEIGHT)
)


# ==========================================
# GRAYSCALE
# ==========================================

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)


# ==========================================
# THRESHOLD
# ==========================================

_, thresh = cv2.threshold(
    gray,
    180,
    255,
    cv2.THRESH_BINARY_INV
)


# ==========================================
# FIND CONTOURS
# ==========================================

contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)


print("Contours detected:", len(contours))


# ==========================================
# FILTER CONTOURS
# ==========================================

contours = [
    contour
    for contour in contours
    if cv2.contourArea(contour) > 15
]


# ==========================================
# SORT CONTOURS
# ==========================================

contours = sorted(
    contours,
    key=cv2.contourArea,
    reverse=True
)


print("Useful contours:", len(contours))


# ==========================================
# TURTLE WINDOW
# ==========================================

screen = turtle.Screen()

screen.setup(
    width=img.shape[1] + 100,
    height=img.shape[0] + 100
)

screen.bgcolor("white")

screen.tracer(0, 0)


# ==========================================
# TURTLE PEN
# ==========================================

pen = turtle.Turtle()

pen.hideturtle()

pen.speed(0)

pen.pensize(1)

pen.color("black")


# ==========================================
# COORDINATE CONVERSION
# ==========================================

def map_point(point):

    x, y = point

    x = x - img.shape[1] / 2

    y = img.shape[0] / 2 - y

    return x, y


# ==========================================
# DRAW IMAGE
# ==========================================

point_counter = 0


for contour in contours:

    points = contour.reshape(-1, 2)

    pen.penup()

    for px, py in points:

        x, y = map_point((px, py))

        pen.goto(x, y)

        pen.pendown()

        point_counter += 1

        if point_counter % UPDATE_EVERY == 0:
            screen.update()

    pen.penup()


# ==========================================
# FINISH
# ==========================================

screen.update()

print("Drawing completed!")

turtle.done()