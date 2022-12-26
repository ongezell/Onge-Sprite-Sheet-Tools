#Developed by Ongezell at Ongezell.com
#Web version available at https://ongezell.com/project/ongespritetools.html

import os
from PIL import Image

folder_path = "IMAGES"
image_file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".png")]
images = [Image.open(path) for path in image_file_paths]
images.sort(key=lambda x: int(os.path.splitext(x.filename)[0].split("-")[-1]))

widths, heights = zip(*(image.size for image in images))
total_width = sum(widths)
max_height = max(heights)

sprite_sheet = Image.new("RGBA", (total_width, max_height))

x_offset = 0
for image in images:
  sprite_sheet.paste(image, (x_offset, 0))
  x_offset += image.size[0]

  sprite_sheet.save("sprite-sheet.png")
