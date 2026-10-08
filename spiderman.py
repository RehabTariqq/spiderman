import cv2
import turtle

IMAGE = "spiderman.png"


img = cv2.imread(IMAGE)


if img is None:
    print("ERROR: spiderman.png was not found.")
    print("Make sure the image is in the same folder as spiderman.py")
    exit()


print("Spider-Man image loaded successfully!")
print("Image width:", img.shape[1])
print("Image height:", img.shape[0])
# Resize image
height = 700

ratio = height / img.shape[0]

width = int(img.shape[1] * ratio)

img = cv2.resize(img, (width, height))

print("Image resized to:", width, "x", height)
# Convert image to grayscale
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)
# Convert grayscale image into
# black and white
_, thresh = cv2.threshold(
    gray,
    180,
    255,
    cv2.THRESH_BINARY_INV
)
# Find contours
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_NONE
)

print("Contours detected:", len(contours))
# Remove very small contours
contours = [
    contour
    for contour in contours
    if cv2.contourArea(contour) > 15
]


# Draw larger contours first
contours = sorted(
    contours,
    key=cv2.contourArea,
    reverse=True
)


print("Useful contours:", len(contours))
# Create Turtle window
screen = turtle.Screen()

screen.setup(
    width=img.shape[1] + 100,
    height=img.shape[0] + 100
)

screen.bgcolor("white")

# Disable automatic screen updates
screen.tracer(0, 0)


# Create drawing turtle
pen = turtle.Turtle()

pen.hideturtle()

pen.speed(0)

pen.pensize(1)

pen.color("black")