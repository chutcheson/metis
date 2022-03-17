from pathlib import Path
from config import IMAGES

# remove empty folders 

# get list of all folders in images directory
folders = [path for path in Path(IMAGES).iterdir()]

# iterate over folders 
for folder in folders:

    # get the images in folders as path objects
    folderImages = [image for image in folder.glob('**/*')]

    print(folderImages)

    if len(folderImages) == 0:

        # delete folder
        folder.rmdir()
