from PIL import Image
from config import IMAGE_TABLE
from csv import reader

def centerCrop(fileName):

    # open image file
    im = Image.open(fileName)
   
    # get image size
    width, height = im.size   

    # get box for crop
    left, top, right, bottom = (width - new_width) / 2, (height - new_height) / 2, (width + new_width) / 2, (height + new_height) / 2

    # crop the center of the image
    im = im.crop((left, top, right, bottom))

    return im
