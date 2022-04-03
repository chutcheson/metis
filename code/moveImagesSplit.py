from config import GRAYSCALE_IMAGES, IMAGE_TABLE, DATA
from pathlib import Path
from csv import reader
from PIL import Image

croppedImagePath = Path(GRAYSCALE_IMAGES)

kerasDirectory = Path(DATA + "/kerasGrayscaleImages")

kerasDirectory.mkdir(exist_ok=True)

blackDirectory = Path(str(kerasDirectory) + "/black")

blackDirectory.mkdir(exist_ok=True)

redDirectory = Path(str(kerasDirectory) + "/red")

redDirectory.mkdir(exist_ok=True)

blackVases = set()

redVases = set()

with open(IMAGE_TABLE, "r") as f:

    table = reader(f)

    for image in table:

        if image[2] == "RED-FIGURE":

            redVases.add(image[0])

        elif image[2] == "BLACK-FIGURE":

            blackVases.add(image[0])

        else:

            pass

for vaseDir in croppedImagePath.iterdir():

    vase = str(vaseDir).split("/")[-1]

    for image in vaseDir.glob("**/*"):

        if str(vase) in blackVases:

            im = Image.open(image)

            im.save(str(blackDirectory) + "/" + str(image).split("/")[-1][:-3] + "jpg")

        elif str(vase) in redVases:

            im = Image.open(image)

            im.save(str(redDirectory) + "/" + str(image).split("/")[-1][:-3] + "jpg")

        else:

            pass
