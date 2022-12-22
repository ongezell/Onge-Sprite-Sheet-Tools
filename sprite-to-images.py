#Developed by Ongezell at Ongezell.com
#Web version available at https://ongezell.com/project/ongespritetools.html
import os
from PIL import Image

# Set the path to the sprite sheet file
sprite_sheet_path = "sprite-sheet.png"

# Load the sprite sheet
sprite_sheet = Image.open(sprite_sheet_path)

# Get the width and height of the sprite sheet
sprite_sheet_width, sprite_sheet_height = sprite_sheet.size

# Prompt the user to enter the output width and height of the images
output_width = int(input("Enter the output width of the images: "))
output_height = int(input("Enter the output height of the images: "))

# Calculate the number of images that will be generated from the sprite sheet
num_images = sprite_sheet_width // output_width

# Create a new folder to hold the images
output_folder_path = "output"
if not os.path.exists(output_folder_path):
  os.makedirs(output_folder_path)

# Split the sprite sheet into individual images
for i in range(num_images):
  x1 = i * output_width
  y1 = 0
  x2 = x1 + output_width
  y2 = output_height
  image = sprite_sheet.crop((x1, y1, x2, y2))
  image.save(os.path.join(output_folder_path, "image-{}.png".format(i)))
