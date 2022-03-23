from config import IMAGE_TABLE_SPLIT, KERAS_IMAGES, TRAINING_IMAGES, VALIDATION_IMAGES
from pathlib import Path
from PIL import Image
from channelHelper import reduceChannels
from tableHelper import getRecords

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

table = getRecords(IMAGE_TABLE_SPLIT)

for imageRecord in table:

    imageName = imageRecord[3].split("/")[-1]

    im = Image.open(imageRecord[3])

    if imageRecord[6] == 3:

        im = reduceChannels(im)

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
