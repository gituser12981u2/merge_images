from PIL import Image
import numpy as np

# Load the images
image2_path = 'images/download.jpg'  # Update to your /images directory path
image1_path = 'images/tree-on-green-lake-1519g7y2yexhnyvl.jpg'  # Update to your /images directory path
image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Ensure both images are the same size
if image1.size != image2.size:
    # Resize second image to match the first
    image2 = image2.resize(image1.size)

# Get the pixels from both images
pixels1 = np.array(image1)
pixels2 = np.array(image2)

# Calculate new dimensions for the output image to be roughly square
num_pixels = image1.size[0] * image1.size[1] * 2  # Total number of pixels from both images
new_width = int(num_pixels**0.5)  # Width is the square root of the total number of pixels
new_height = (num_pixels + new_width - 1) // new_width  # Ensure all pixels fit into the new image

# Initialize the new image with black pixels
new_image = Image.new('RGB', (new_width, new_height), "black")
new_pixels_array = np.array(new_image)

# Iterate over each pixel and set them in the new image's array
idx = 0
for y in range(image1.size[1]):
    for x in range(image1.size[0]):
        # Get the new x and y coordinates in the output image
        new_x = idx % new_width
        new_y = idx // new_width
        new_pixels_array[new_y, new_x] = pixels1[y, x]  # Set pixel from the first image
        idx += 1
        # Calculate new x and y coordinates for the next pixel
        new_x = idx % new_width
        new_y = idx // new_width
        new_pixels_array[new_y, new_x] = pixels2[y, x]  # Set pixel from the second image
        idx += 1

# Convert the array back to an Image object and save
new_image = Image.fromarray(new_pixels_array)
output_path = 'output/merged_pixels_image.jpg'  # Update to your /output directory path
new_image.save(output_path)
