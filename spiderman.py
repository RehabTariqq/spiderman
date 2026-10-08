import cv2


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
