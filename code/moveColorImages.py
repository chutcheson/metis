from config import IMAGE_TABLE_SPLIT, KERAS_IMAGES, TRAINING_IMAGES, VALIDATION_IMAGES
from pathlib import Path
from PIL import Image
from channelHelper import reduceChannels
from tableHelper import getRecords
from numpy import asarray
from tensorflow.keras.preprocessing.image import smart_resize

# create directories for Keras
# kerasImages /
#   training /
#       RED_FIGURE /
#       BLACK_FIGURE /
#   validation /
#       RED_FIGURE /
#       BLACK_FIGURE /

kerasImagesPath = Path(KERAS_IMAGES)
kerasImagesPath.mkdir(exist_ok=True)

trainingImagesPath = Path(TRAINING_IMAGES)
trainingImagesPath.mkdir(exist_ok=True)

validationImagesPath = Path(VALIDATION_IMAGES)
validationImagesPath.mkdir(exist_ok=True)

RFTImagesPath = trainingImagesPath / "RED_FIGURE"
RFTImagesPath.mkdir(exist_ok=True)

BFTImagesPath = trainingImagesPath / "BLACK_FIGURE"
BFTImagesPath.mkdir(exist_ok=True)

RFVImagesPath = validationImagesPath / "RED_FIGURE"
RFVImagesPath.mkdir(exist_ok=True)

BFVImagesPath = validationImagesPath / "BLACK_FIGURE"
BFVImagesPath.mkdir(exist_ok=True)

# get image table records
table = getRecords(IMAGE_TABLE_SPLIT)

# iterate over image table records
for imageRecord in table:

    # get image file name
    imageName = imageRecord[3].split("/")[-1][:-3] + "jpg"

    # open image file
    im = Image.open(imageRecord[3])

    # check channel count
    if imageRecord[6] == "3":

        # if channel count == 3 reduce to 0
        im = reduceChannels(im)

    im = asarray(im)
    im = im.reshape(im.shape + (1,))
    im = smart_resize(im, (224,224))
    im = im.reshape((224,224))
    im = Image.fromarray(im)
    im = im.convert("L")

    # check train or validation and place in correct folder
    if imageRecord[8] == "training":

        if imageRecord[1] == "RED-FIGURE":

            im.save(str(RFTImagesPath / imageName))

        else:

            im.save(str(BFTImagesPath / imageName))

    else:

        if imageRecord[1] == "RED-FIGURE":

            im.save(str(RFVImagesPath / imageName))

        else:

            im.save(str(BFVImagesPath / imageName))
