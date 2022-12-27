import argparse
import os

from PIL import Image

def create_sprite_sheet(images, columns, output_file):
    # Determine the number of rows based on the number of images and the number of columns
    rows = (len(images) + columns - 1) // columns

    # Determine the width and height of each cell
    cell_width = images[0].width
    cell_height = images[0].height
    sprite_width = cell_width * columns
    sprite_height = cell_height * rows

    # Create a new image to hold the sprite sheet
    sprite_sheet = Image.new('RGBA', (sprite_width, sprite_height))

    # Iterate over the rows and columns and paste the images onto the sprite sheet
    for row in range(rows):
        for column in range(columns):
            # Determine the index of the current image
            index = row * columns + column
            if index >= len(images):
                # No more images, stop pasting
                break
            # Paste the image onto the sprite sheet
            sprite_sheet.paste(images[index], (column * cell_width, row * cell_height))

    # Save the sprite sheet
    sprite_sheet.save(output_file)

if __name__ == '__main__':
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', help='the directory containing the input image files')
    parser.add_argument('--columns', type=int, default=1, help='the number of columns in the sprite sheet')
    parser.add_argument('--output', default='sprite_sheet.png', help='the output file')
    args = parser.parse_args()

    # Load the images from the specified directory
    images = []
    for file in os.listdir(args.directory):
        if file.endswith('.png') or file.endswith('.jpg'):
            images.append(Image.open(os.path.join(args.directory, file)))

    # Create the sprite sheet
    create_sprite_sheet(images, args.columns, args.output)
