import os
import random
from PIL import Image

folder_path = r'C:\Users\dhana\Pictures\LINKED NEW'  # Replace with the actual folder path
file_names = os.listdir(folder_path)
one = random.choice(file_names)
base_image = Image.open(r'C:\Users\dhana\Pictures\LINKED NEW\doctor (1).png').convert("RGBA")

one = random.choice(file_names)
# Open the overlay image
overlay_image = Image.open(os.path.join(folder_path, one)).convert("RGBA")


# Define the desired width and height for the overlay image
overlay_width = 800
overlay_height = 800

# Resize the overlay image
overlay_image = overlay_image.resize((overlay_width, overlay_height))

# Define the position where the overlay image should be pasted on the base image
overlay_position = (600, 500)  # Coordinates (x, y) from the top-left corner of the base image

# Create a new blank image with transparent background, matching the size of the base image
composite_image = Image.new("RGBA", base_image.size)

# Paste the base image onto the composite image
composite_image.paste(base_image, (0, 0))

# Paste the resized overlay image onto the composite image at the specified position
composite_image.paste(overlay_image, overlay_position, mask=overlay_image)

# Save the composite image
composite_image.save("output_image.png")

# Open the image
image = Image.open("output_image.png")

# Display the image
image.show()




'''# Get a list of file names in the folder
file_names = os.listdir(folder_path)

# Iterate over the file names
for file_name in file_names:
    # Construct the full path to the image file
    file_path = os.path.join(folder_path, file_name)

    # Open the image
    image = Image.open(file_path)
    image.show()

    # Perform operations on the image
    # ...

    # Close the image
    image.close()
'''