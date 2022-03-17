from xml.etree.ElementTree import parse
from pathlib import Path
from config import MANIFEST, DATA, IMAGES, COLLECT_LOGS
from requests import get

# create XML tree of vases
tree = parse(MANIFEST)

# initialize image count
imageCount = 0

# start
start = False

# iterate over vases
for vase in tree.getroot():

    if not vase.attrib:

        continue

    if vase.attrib['id'].lstrip("{").rstrip("}") == "09986FF0-EA7C-40B6-8917-D30ADB8603E6":

            start = True

    if not start:

        continue

    # create path at which to store vase images for particular vase
    vasePathName = IMAGES + vase.attrib['id'].lstrip("{").rstrip("}")

    # create path object for vase
    vasePath = Path(vasePathName)

    # make directory for vase images of particular vase
    vasePath.mkdir(exist_ok=True)    
    
    # iterate over vase attributes
    for attribute in vase:

        # check for image records
        if attribute.tag == "Image-Record":
            
            # iterate over image record attributes
            for attr in attribute:
                        
                # if the attribute is the image file name
                if attr.tag == "Filename":

                    # get the image
                    image = get(f"https://www.beazley.ox.ac.uk/Vases/SPIFF/{attr.text}cc001001.jpe")

                    # open file to store the image
                    with open(vasePathName + "/" + str(imageCount) + ".jpe", "wb") as f:
                        
                        # write image to file
                        f.write(image.content)

                    # increment image counter
                    imageCount += 1
