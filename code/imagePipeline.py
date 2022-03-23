from config import MANIFEST, IMAGES, IMAGE_TABLE_SPLIT
from tableHelper import xmlToVaseDict, makeTableRecords, recordsToTable
from imageDirectoryHelper import getVaseImages, getImageMetadata 
from filterImageHelper import filterSize, filterColor
from splitHelper import getVaseTypes, performSplit 

size = 224
color = "GRAYSCALE"

# get metadata associated with vases
# takes xml manifest
# returns { vase : ['9BFE5BF6-F6DE-413C-880C-E74F9D0E61B0', 'BLACK-FIGURE', 'GREECE'] }
vaseDict = xmlToVaseDict(MANIFEST)

# get images associated with vases
# takes path to images with sub-directory for each vase
# returns { vase : '../data/images/9BFE5BF6-F6DE-413C-880C-E74F9D0E61B0/16a58831602b3e3cb928789324063c5f.jpe' }
vaseImages = getVaseImages(IMAGES)

# combine vaseDict and vaseImages to make imageRecords
# returns [['9BFE5BF6-F6DE-413C-880C-E74F9D0E61B0', 'BLACK-FIGURE', 'GREECE', '../data/images/9BFE5BF6-F6DE-413C-880C-E74F9D0E61B0/16a58831602b3e3cb928789324063c5f.jpe']]
imageRecords = makeTableRecords(vaseDict, vaseImages)

# iterate over imageRecords 
# creates ['9BFE5BF6-F6DE-413C-880C-E74F9D0E61B0', 'BLACK-FIGURE', 'GREECE', 
# / '../data/images/9BFE5BF6-F6DE-413C-880C-E74F9D0E61B0/16a58831602b3e3cb928789324063c5f.jpe', 574, 602, 3, 'GRAYSCALE']
for imageRecord in imageRecords:

    # add shape and coloration
    imageRecord.extend(getImageMetadata(imageRecord[-1]))

# eliminate all images with a height or width < size
imageRecords = filterSize(imageRecords, size)

# eliminate all images that are not of the proper color type (GRAYSCALE, COLOR)
imageRecords = filterColor(imageRecords, color)

# splits vases into redVase set and blakcVase set
redVases, blackVases = getVaseTypes(vaseDict, vaseImages)

# splits vases into training vases and validation vases
train, validation = performSplit(redVases, blackVases)

# adds selection to imageRecords
# removes record if not redVase or blackVase
newImageRecords = []

# iterate over imageRecords
for imageRecord in imageRecords:

    if imageRecord[0] in train:

        # append record + "training" to newImageRecords
        newImageRecords.append(imageRecord + ['training'])

    elif imageRecord[0] in validation:

        # append record + "validation" to newImageRecords
        newImageRecords.append(imageRecord + ['validation'])

    else:

        pass

# overwrite imageRecords
imageRecords = newImageRecords

recordsToTable(imageRecords, IMAGE_TABLE_SPLIT)
