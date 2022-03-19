from PIL import Image
from config import DATA, IMAGE_TABLE
from collections import defaultdict
from csv import reader
from pathlib import Path

def centerCrop(fileName, new_height, new_width):

    # open image file
    im = Image.open(fileName)
   
    # get image size
    width, height = im.size   

    # get box for crop
    left, top, right, bottom = (width - new_width) / 2, (height - new_height) / 2, (width + new_width) / 2, (height + new_height) / 2

    # crop the center of the image
    im = im.crop((left, top, right, bottom))

    return im

vaseImages = defaultdict(list)

with open(IMAGE_TABLE, "r") as f:

    for image in reader(f):

        if int(image[4]) < 244 or int(image[5]) < 244 or int(image[6]) != 3:

            pass

        else:

            vaseImages[image[0]].append(image[1])

cropPath = Path(DATA + "croppedImages")

cropPath.mkdir(exist_ok=True)

for key in vaseImages:

    vasePath = Path(DATA + "croppedImages/" + key)

    vasePath.mkdir(exist_ok=True)

    for image in vaseImages[key]:

        im = centerCrop(image, 244, 244)

        im.save(DATA + "croppedImages/" + key + "/" + image.split("/")[-1])

