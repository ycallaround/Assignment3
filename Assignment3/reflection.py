"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    # TODO: your code here.
    # enlarging the size of the image to times 2 the Y axis
    image = enlarge_image_height(image)
    # running a nested for loop copy and paste pixel
    for x in range(image.width):
        for y in range(image.height // 2):
            image.set_pixel(x, image.height - y -1, image.get_pixel(x, y))
            # copying top to bottom

    return image

def enlarge_image_height(image):
    # function that get the ole image and return new image the the bottom half is blank and the height is double
    new_image = SimpleImage.blank(image.width, image.height * 2)
    for x in range(image.width):
        for y in range(image.height):
            new_image.set_pixel(x,y,image.get_pixel(x,y))
    return new_image

def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
