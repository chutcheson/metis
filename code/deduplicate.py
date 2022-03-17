from pathlib import Path
from config import IMAGES
from hashlib import md5

# This script removes duplicate images in folders
# It also removes duplicate images across folders

# define function to get md5sum of jpe images
# takes a fileName returns an md5sum as a str
def md5file(fileName):

    # open the file located at fileName to be accessed as bytes
    with open(fileName, "rb") as f:

        # create an md5 object
        fileHash = md5()
    
        # iteratve over file reading bytes
        while chunk := f.read(8192):
            
            # provide bytes to md5 object
            fileHash.update(chunk)

    # return md5 hash as a string
    return fileHash.hexdigest()

# get list of folders in IMAGES
folders = [path for path in Path(IMAGES).glob('**/*')]

# create a dictionary to store seen md5 sums accross vases 
seenInPriorFolder = {}

# create a set to store original path of images seen more than once across vases
seenMoreThanOnce = set()

# iterate over folders 
for index, folder in enumerate(folders):

    # get the images in folders as path objects
    folderImages = [image for image in folder.glob('**/*')]

    # get the hash for each images
    hashes = [md5file(str(image)) for image in folderImages]

    # create a dictionary to store images seen in folder
    seenInFolder = {}

    # iterate over each image, hash pair
    for image, h in zip(folderImages, hashes):
       
        if h in seenInPriorFolder:

            # add to list of images seen across folders 
            seenMoreThanOnce.add(seenInPriorFolder[h])

            # remove image
            image.unlink()

        elif h in seenInFolder:

            # remove image
            image.unlink()

        else:

            # create new name for image
            newPathName = "/".join(str(image).split("/")[:-1]) + "/" + h + ".jpe"

            # add new path name to seen in folder dict
            seenInFolder[h] = newPathName

            # create new path for image
            newPath = Path(newPathName)

            # rename image
            image.rename(newPath)

    # extend seen in prior folder dict with images from current folder
    seenInPriorFolder.update(seenInFolder)

# iterate over first instance of files seen in multiple folders
for imagePathName in seenMoreThanOnce:

    # creaet a path for that image
    imagePath = Path(imagePathName)

    # delete the file
    imagePath.unlink()

