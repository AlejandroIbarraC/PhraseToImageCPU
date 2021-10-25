import numpy as np

from PIL import Image

# Image file name
source_fn = "imagen.txt"

# Pixel height and width of resulting image
height = 114
width = 240


# Reads image text file and creates an exported B/W JPG
def convert_image():
    # Read lines from image txt
    print("Reading lines from txt...")
    lines = open(source_fn).read().splitlines()
    print(lines)

    # Convert lines STR array to INT numpy array
    print("Converting lines array to numpy array...")
    lines = np.fromiter(lines, dtype=int)
    print(lines)

    # Reshape array to fit and multiply by 255 to set white values
    print("Reshaping array to fit matrix...")
    lines = lines.reshape(height, width) * 255
    print(lines)

    # Convert array to image
    print("Converting array matrix to exported image JPG...")
    im = Image.fromarray(lines)
    im = im.convert("RGB")

    return im


if __name__ == '__main__':
    img = convert_image()
    img.save("result.jpg")
    print("Done!")