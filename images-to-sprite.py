#Developed by Ongezell at Ongezell.com
#Web version available at https://ongezell.com/project/ongespritetools.html

import os
from PIL import Image

# Set the path to the folder containing the images
folder_path = "IMAGES"

# Get a list of all the image file paths in the folder
image_file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".png")]

# Load the images and get their sizes
images = [Image.open(path) for path in image_file_paths]

# Sort the images based on their file names
images.sort(key=lambda x: int(os.path.splitext(x.filename)[0].split("-")[-1]))

widths, heights = zip(*(image.size for image in images))

# Calculate the size of the sprite sheet
total_width = sum(widths)
max_height = max(heights)

# Create a new image to hold the sprite sheet
sprite_sheet = Image.new("RGBA", (total_width, max_height))

# Paste the images onto the sprite sheet
x_offset = 0
for image in images:
  sprite_sheet.paste(image, (x_offset, 0))
  x_offset += image.size[0]

# Save the sprite sheet to a file
sprite_sheet.save("sprite-sheet.png")
