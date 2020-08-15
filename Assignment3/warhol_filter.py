"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

DEFAULT_FILE = 'images/simba-sq.jpg'

def main():
    print('Welcome to Warhol filter. Please follow instructions.')
    # Choosing file
    patch_name = get_file()
    # Deciding row number
    n_rows = get_rows()
    # Deciding columns number
    n_cols = get_cols()
    final_image = creat_final_image(patch_name,n_cols,n_rows)
    # function that goes through all spots and ask for ratio for each of the patches
    final_image = multiply_me(final_image,patch_name,n_rows,n_cols)
    # This is an example which should generate a pinkish patch
    # patch = make_recolored_patch(1.5, 0, 1.5)
    final_image.show()

def creat_final_image(patch_name,n_cols,n_rows):
    patch = SimpleImage(patch_name)
    patch_size_w = patch.width
    patch_size_h = patch.height
    final_image = SimpleImage.blank(n_cols * patch_size_w, n_rows * patch_size_h)
    return final_image

def multiply_me(final_image,patch_name,n_rows,n_cols):
    # run through 6 iteration and creat filter per cube
    patch = SimpleImage(patch_name)
    print('For original picture, set ratios to 1')
    want_control = input('Do you want to control the color ratios ? (y/n)')
    for r in range(n_rows):
        for c in range(n_cols):
            if want_control == 'y':
                # requests ratios per color per cube
                red_scale = float(input('Please enter red ratio between 0 to 2 for patch in location (' + str(r + 1) + ',' + str(c + 1) + '):'))
                green_scale = float(input('Please enter green ratio between 0 to 2 for patch in location (' + str(r + 1) + ',' + str(c + 1) + '):'))
                blue_scale = float(input('Please enter blue ratio between 0 to 2 for patch in location (' + str(r + 1) + ',' + str(c + 1) + '):'))
            else:
                # randomize the float ratio
                red_scale = random.uniform(0,2)
                green_scale = random.uniform(0,2)
                blue_scale = random.uniform(0,2)
            # calling to create a version of patch or reflection
            rand_for_me = random.randint(1,3)
            patch = SimpleImage(patch_name)
            if rand_for_me == 1:
                patch = make_recolored_patch(red_scale, green_scale, blue_scale,make_reflected(patch_name))
            else:
                patch = make_recolored_patch(red_scale, green_scale, blue_scale,patch)
            # calling a function that paste the patch
            final_image = paste_patch(r,c,patch,final_image)
    # after 6 rounds, return full image
    return final_image


def paste_patch(r,c,patch,final_image):
    # pasting the patch in the right location
    for x in range(patch.width):
        for y in range(patch.height):
            final_image.set_pixel(x + c * patch.width, y + r * patch.height, patch.get_pixel(x, y))
    return final_image

def make_recolored_patch(red_scale, green_scale, blue_scale,patch):
    # get the ratios and the image, and return a new version of the image after color manipulations
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    for pixel in patch:
        pixel.red = int(pixel.red * red_scale)
        pixel.green = int(pixel.green * green_scale)
        pixel.blue = int(pixel.blue * blue_scale)
    return patch

def make_reflected(patch_name):
    # make a reflection version of the patch. get the name of the patch, return an upside-down image
    old_image = SimpleImage(patch_name)
    # old image of the patch
    new_image = SimpleImage.blank(old_image.width, old_image.height)
    # new blank image
    # running a nested for loop copy and paste pixel
    for x in range(old_image.width):
        for y in range(old_image.height):
            new_image.set_pixel(x, old_image.height - y -1, old_image.get_pixel(x, y))
            # copying top to bottom
    return new_image

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename

def get_rows():
    # Read image file path from user, or use the default file
    rows = input('Enter image rows (or press enter for random number): ')
    if rows == '':
        rows = random.randint(1,5)
    else:
        rows = int(rows)
    return rows
def get_cols():
    # Read image file path from user, or use the default file
    cols = input('Enter image cols (or press enter for random number): ')
    if cols == '':
        cols = random.randint(1,5)
    else:
        cols = int(cols)
    return cols


if __name__ == '__main__':
    main()