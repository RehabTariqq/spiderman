
import cv2
import turtle
import time

IMAGE = "spiderman.png"
HEIGHT = 700
UPDATE_EVERY = 1
DELAY = 0.03

print("Spider-Man Contour Tracer")
print("Loading image...")

img = cv2.imread(IMAGE)

if img is None:
    print("ERROR: spiderman.png was not found.")
    print("Place it in the same folder as spiderman.py.")
    raise SystemExit(1)

print("Spider-Man image loaded successfully!")

ratio = HEIGHT / img.shape[0]
width = int(img.shape[1] * ratio)
img = cv2.resize(img, (width, HEIGHT))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_LIST,
    cv2.CHAIN_APPROX_NONE
)

print("Contours detected:", len(contours))

contours = [
    contour
    for contour in contours
    if cv2.arcLength(contour, False) > 15
]

contours = sorted(
    contours,
    key=cv2.contourArea,
    reverse=True
)

print("Useful contours:", len(contours))

screen = turtle.Screen()
screen.setup(width=width + 100, height=HEIGHT + 100)
screen.title("Spider-Man Drawing Animation")
screen.bgcolor("white")
screen.tracer(0, 0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(1)
pen.color("black")


def map_point(point):
    x, y = point
    x -= width / 2
    y = HEIGHT / 2 - y
    return x, y


point_counter = 0

for contour in contours:
    points = contour.reshape(-1, 2)

    if len(points) == 0:
        continue

    pen.penup()

    for px, py in points:
        x, y = map_point((px, py))
        pen.goto(x, y)
        pen.pendown()

        point_counter += 1

        if point_counter % UPDATE_EVERY == 0:
            screen.update()
            time.sleep(DELAY)

    pen.penup()

screen.update()

print("Drawing completed!")
print("Total points drawn:", point_counter)

turtle.done()