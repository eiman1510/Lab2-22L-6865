import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

try:
    img = Image.open("pic2.jpg")
    numpy_array = np.array(img)
    print(numpy_array.shape)

    # Plot the Original Image
    plt.imshow(numpy_array)
    plt.axis('off')
    plt.title('Original Image')
    plt.show()

    # Rotate the Image
    rotated_array = np.rot90(numpy_array)
    plt.imshow(rotated_array)
    plt.axis('off')
    plt.title('Rotated Image')
    plt.show()

    # Flip the Image Horizontally
    flipped_array = np.fliplr(numpy_array)
    plt.imshow(flipped_array)
    plt.axis('off')
    plt.title('Flipped Image')
    plt.show()

    # Apply Grayscale Filter
    def grayscale(rgb):
        return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

    gray_array = grayscale(numpy_array)

    plt.imshow(gray_array, cmap=plt.get_cmap('gray'))  # Use a grayscale colormap
    plt.axis('off')
    plt.title('Grayscale Image')
    plt.show()

except FileNotFoundError:
    print("Error: The image file 'pic.jpg' was not found.  Make sure it's in the same directory as your script, or provide the correct path.")
except Exception as e:
    print(f"An error occurred: {e}")
