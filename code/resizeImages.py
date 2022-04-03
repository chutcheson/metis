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
    
    # return cropped image
    return im

# create a { vase : list of file paths } dictionary to store vase image file paths
vaseImages = defaultdict(list)

# open the image table csv
with open(IMAGE_TABLE, "r") as f:

    # iterate over the image table records
    for image in reader(f):

        if int(image[4]) < 244 or int(image[5]) < 244 or int(image[6]) != 3:

            # if the image is smaller than 224 x 224 or has less than 3 channels skip
            pass

        else:

            # otherwise save image filepath
            vaseImages[image[0]].append(image[1])

# create a directory path object to store cropped images
cropPath = Path(DATA + "croppedImages")

# create a directory to store cropped images
cropPath.mkdir(exist_ok=True)

# iterate over vases
for key in vaseImages:

    # create a path object for each vase
    vasePath = Path(DATA + "croppedImages/" + key)

    # create a directory for each vase
    vasePath.mkdir(exist_ok=True)

    # iteratve over the vase images
    for image in vaseImages[key]:

        # crop the image
        im = centerCrop(image, 224, 224)

        # save the image in the vase path
        im.save(DATA + "croppedImages/" + key + "/" + image.split("/")[-1])

        break

