import os

directory = r"C:\Users\dhana\Pictures\full_images"

x = os.listdir(directory)

t = [i for i in x if i.endswith('.jpg')]

print(t)

import random
import glob

# Specify the path to the folder containing PNG images
folder_path = r'C:\Users\dhana\Pictures\animated_images'

# Get a list of all PNG files in the folder
png_files = glob.glob(folder_path + '/*.png')




for i in range(5):
    from PIL import Image

    # Randomly select one PNG file
    selected_file = random.choice(png_files)
    selected_file1 = random.choice(png_files)

    # Print the selected file
    print(selected_file)

    # Open the background image
    background_image = Image.open(t[i])

    # Open the overlay image
    overlay_image = Image.open(selected_file)
    overlay_image1 = Image.open(selected_file1)

    # Adjust the size of the overlay image
    overlay_width, overlay_height = overlay_image.size
    new_overlay_width = int(overlay_width * 2)  # Adjust the size as needed
    new_overlay_height = int(overlay_height * 2)  # Adjust the size as needed
    resized_overlay_image = overlay_image.resize((new_overlay_width, new_overlay_height))
    resized_overlay_image1 = overlay_image1.resize((new_overlay_width, new_overlay_height))

    # Calculate the position to place the overlay image on the background image
    position = (750, 800)  # Adjust the position as needed
    position1 = (50, 800)

    # Paste the overlay image onto the background image
    background_image.paste(resized_overlay_image, position, resized_overlay_image)
    background_image.paste(resized_overlay_image1, position1, resized_overlay_image1)

    # Save the final image
    background_image.save(r"C:\Users\dhana\Pictures\images_for_linked_in_post"+"\\"+ f"output_image{i}.jpg")

    Image.open(r"C:\Users\dhana\Pictures\images_for_linked_in_post"+"\\"+ f"output_image{i}.jpg").show()

