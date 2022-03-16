from xml.etree.ElementTree import parse
from pathlib import Path
from config import MANIFEST, DATA, IMAGES
from requests import get
from collections import Counter

# create XML tree of vases
tree = parse(MANIFEST)

# initialize image count
imageCount = 0
provVases = set()
totalVases = set()
vases = set()
provenancesCounter = Counter()

# iterate over vases
for vase in tree.getroot():

    if vase.attrib:

        vaseId = vase.attrib['id']

        totalVases.add(vaseId)

        # iterate over vase attributes
        for attribute in vase:

            if attribute.tag == "Provenance" and attribute.text is not None:

              provVases.add(vaseId)

              vaseProv = attribute.text

            # check for image records
            if attribute.tag == "Image-Record":
                
                # iterate over image record attributes
                for attr in attribute:
                    
                    # if the attribute is the image file name
                    if attr.tag == "Filename":

                        # increment image counter
                        imageCount += 1

                        if vase.attrib['id'] not in vases and vase.attrib['id'] in provVases:

                            provenancesCounter[vaseProv.split(" ")[0].rstrip(",")] += 1

                        vases.add(vase.attrib['id'])

print(f"total vases: {len(totalVases)}")
print(f"vases with images: {len(vases)}")
print(f"total provenances: {len(provVases)}")
print(f"total images: {imageCount}")
print(f"total vases with images & provenances: {len(provVases & vases)}")
print(f"provenances count: {provenancesCounter}")
