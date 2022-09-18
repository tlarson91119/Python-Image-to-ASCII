from PIL import Image
import math

# Average RGB to Single Brightness Value
def getBrightness(pixel):
    avg = 0
    if type(pixel) is tuple:
        avg = (pixel[0] + pixel[1] + pixel[2]) / 3.0
        return round(avg)
    return -1

# Convert Brightness to ASCII
def getLetter(value):
    if value <= 0 or value > 255:
        return " "  # Default Character

    asciiLetters = "$O+-. $"    # Available characters to use

    letter = round((value / 255) * len(asciiLetters))
    return asciiLetters[letter-1]

# Open an image file - on successful execution, store handler in img
try:
    # Open file for binary read
    img = Image.open("clint.png", mode='r')
except FileNotFoundError:
    print("Failed to open file...\n")
    exit(1)
except:
    print("Something went wrong")
    exit(2)
else:
    print("Successfully loaded image!\n")

width, height = img.size
print("Size =", width, "x", height)
print("Number of pixels =", width * height)

# Prepare ASCII Array
asciiArray = []
for i in range(width):
    inner = []
    for j in range(height):
        inner.append(0)
    asciiArray.append(inner)

# Convert pixels to ASCII and Store in asciiArray
for y in range(height):
    for x in range(width):
        brightness = getBrightness( img.getpixel((x, y)) )
        asciiArray[x][y] = getLetter( brightness )

# Print to Console: Uncomment below to show results in terminal
# for y in range(height):
#     for x in range(width):
#         print(asciiArray[x][y]+asciiArray[x][y],end="")
#     print()
# print("End of Image")

# Write To File
print("Writing to File out.txt")
fImage = open("out.txt", "w")
for y in range(height):
    for x in range(width):
        fImage.write(asciiArray[x][y]+asciiArray[x][y]+asciiArray[x][y])
    fImage.write("\n")

fImage.close()
print("Done...")