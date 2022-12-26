#Developed by Ongezell at Ongezell.com
#Web version available at https://ongezell.com/project/ongespritetools.html
import os
from PIL import Image

sprite_sheet_path = "sprite-sheet.png"
sprite_sheet = Image.open(sprite_sheet_path)

sprite_sheet_width, sprite_sheet_height = sprite_sheet.size
output_width = int(input("Enter the output width of the images: "))
output_height = int(input("Enter the output height of the images: "))
num_images = sprite_sheet_width // output_width


output_folder_path = "output"
if not os.path.exists(output_folder_path):
  os.makedirs(output_folder_path)

for i in range(num_images):
  x1 = i * output_width
  y1 = 0
  x2 = x1 + output_width
  y2 = output_height
  image = sprite_sheet.crop((x1, y1, x2, y2))
  image.save(os.path.join(output_folder_path, "image-{}.png".format(i)))
