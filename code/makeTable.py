from xml.etree.ElementTree import parse
from pathlib import Path
from config import MANIFEST, DATA, IMAGES, COLLECT_LOGS
from collections import defaultdict
from csv import writer

# this file uses the manifest and image files
# to create a csv with depicted vase fabric, technique and provenance for vase images

# create dict to store IDs of vases with images and list of file paths
vases = defaultdict(list)

# create path object for images folder
imagesFolder = Path(IMAGES)

# iterate over the folder representing each vase
for path in imagesFolder.iterdir():

    # get image files
    for f in path.glob("**/*"):

        # use identifier as key and add file path
        vases[str(path).split("/")[-1]].append(str(f))

# create table for vase images
vaseFileTable = []

# create XML tree of vases
tree = parse(MANIFEST)

# iterate over vases
for vase in tree.getroot():

    # initialize fabric field 
    fabric = None
    
    # initialize technique field
    technique = None
    
    # initialize provenance field
    provenance = None

    # check for vase id
    if not vase.attrib:

        # continue if no id
        continue

    # remove brackets around vase id
    vaseID = vase.attrib['id'].lstrip("{").rstrip("}")

    # check to see that there are images for vase
    if vaseID not in vases:

        # continue if no images
        continue

    # iterate over vase attributes
    for child in vase:

        # check for fabric
        if child.tag == "Fabric":

            fabric = child.text

        # check for technique
        elif child.tag == "Technique":

            technique = child.text

        # check for provenance
        elif child.tag == "Provenance":

            provenance = child.text

        else:

            pass

    # if all fields were present 
    if fabric and technique and provenance:

        # iterate over vase images
        for image in vases[vaseID]:

            # add a row to vaseFileTable with vase info
            vaseFileTable.append([vaseID, image, fabric, technique, provenance.split(",")[0]])

# open a file to save vaseFileTable
with open(DATA + "imageInfo.csv", "w") as f:

    # create csv writer
    datawriter = writer(f)

    # iterate over vaseFileTable rows
    for row in vaseFileTable:

        # write rows to csv
        datawriter.writerow(row)

