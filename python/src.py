from PIL import Image
import numpy as np

# Load the images
image1_path = 'images/download.jpg'
image2_path = 'images/tree-on-green-lake-1519g7y2yexhnyvl.jpg'
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Ensure both images are the same size
if image1.size != image2.size:
    # Resize second image to match the first
    image2 = image2.resize(image1.size)

# Get the pixels from both images
pixels1 = np.array(image1)
pixels2 = np.array(image2)

# Initialize the new image with black pixels
new_image = Image.new('RGB', (pixels1.shape[1] * pixels1.shape[0] * 2, 1), "black")
new_pixels = new_image.load()

# Iterate over each pixel and set them in the new image
idx = 0
for y in range(pixels1.shape[0]):
    for x in range(pixels1.shape[1]):
        # Set pixels from the first image
        new_pixels[idx, 0] = tuple(pixels1[y, x])
        idx += 1
        # Set pixels from the second image
        new_pixels[idx, 0] = tuple(pixels2[y, x])
        idx += 1

# Save the output image
output_path = 'output/merged_pixels_image.jpg'
new_image.save(output_path)
output_path
