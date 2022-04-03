from pathlib import Path
from numpy import asarray, array_equal
from collections import defaultdict
from PIL import Image

# getVaseImages takes a directory with subdirectories for each vase
# getVase returns a dictionary of vase : List[images]

def getVaseImages(directory):

    # create dict to store IDs of vases with images and list of file paths
    vases = defaultdict(list)

    # create path object for images folder
    imagesFolder = Path(directory)

    # iterate over the folder representing each vase
    for path in imagesFolder.iterdir():

        # get image files
        for f in path.glob("**/*"):

            # use identifier as key and add file path
            vases[str(path).split("/")[-1]].append(str(f))

    return vases

def getImageMetadata(imageFile):

    # get image as numpy array
    imageArray = asarray(Image.open(imageFile))

    # set image height
    height = imageArray.shape[0]
    
    # set image width
    width = imageArray.shape[1]

    # check if image has channels
    if len(imageArray.shape) == 3:

        # get image channels
        channels = imageArray.shape[2]

        if array_equal(imageArray[:,:,0], imageArray[:,:,1]) and array_equal(imageArray[:,:,0], imageArray[:,:,2]):

            # if all channels are equal then image is grayscale
            color = "GRAYSCALE"

        else:

            # otherwise image is color
            color = "COLOR"

        return [*imageArray.shape, color]

    else:

        # if no channels
        channels = 0
        
        # if no channels then image is grayscale
        color = "GRAYSCALE"

        return [*imageArray.shape, channels, color]


