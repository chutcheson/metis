from xml.etree.ElementTree import parse
from pathlib import Path
from config import MANIFEST, DATA, IMAGES, COLLECT_LOGS
from collections import defaultdict
from csv import writer

# create set to store IDs of vases with images
vases = defaultdict(list)

# create path object for images folder
imagesFolder = Path(IMAGES)

# iterate over the folder representing each vase
for path in imagesFolder.iterdir():

    for f in path.glob("**/*"):

        vases[str(path).split("/")[-1]].append(str(f))

# create table for vase images

vaseFileTable = []

# create XML tree of vases
tree = parse(MANIFEST)

# iterate over vases
for index, vase in enumerate(tree.getroot()):

    fabric = None
    technique = None
    provenance = None

    if not vase.attrib:

        # continue if vase has no id
        continue

    # reformat vase id
    vaseID = vase.attrib['id'].lstrip("{").rstrip("}")

    if vaseID not in vases:

        # continue if vase is not in the set of vases with images
        continue

    for child in vase:

        if child.tag == "Fabric":

            fabric = child.text

        elif child.tag == "Technique":

            technique = child.text

        elif child.tag == "Provenance":

            provenance = child.text

        else:

            pass

    if fabric and technique and provenance:

        for image in vases[vaseID]:

            vaseFileTable.append([vaseID, image, fabric, technique, provenance.split(",")[0]])

with open(DATA + "imageInfo.csv", "w") as f:

    datawriter = writer(f)

    for row in vaseFileTable:

        datawriter.writerow(row)

print(vaseFileTable[:2])
