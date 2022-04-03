from xml.etree.ElementTree import parse
from config import MANIFEST, DATA, IMAGES, IMAGE_TABLE_SPLIT
from tableHelper import getRecords
from csv import reader, writer

# This file produces a record that can be checked

def getMismatchRecords(mismatchFile):

    records = {}

    with open(mismatchFile, "r") as f:

        for row in reader(f):

            records[row[0]] = row

    return records

# get training records

mismatchRecords = getMismatchRecords("../data/training_diffs.csv")
mismatchRecords.update(getMismatchRecords("../data/validation_diffs.csv"))

# get table records

tableRecords = getRecords(IMAGE_TABLE_SPLIT)

mRecords = {}

for row in tableRecords:

    fileName = row[3].split("/")[-1][:-3] + "jpg"

    if fileName in mismatchRecords:

        mRecords[row[0]] = [row[0]] + mismatchRecords[fileName]

mismatchRecords = mRecords

# create XML tree of vases
tree = parse(MANIFEST)

# iterate over vases
for vase in tree.getroot():

    if not vase.attrib:

        continue

    # create path at which to store vase images for particular vase
    vaseID = vase.attrib['id'].lstrip("{").rstrip("}")

    for attribute in vase:

        if attribute.tag == "Vase-Number":

            if vaseID in mismatchRecords:

                mismatchRecords[vaseID].append(attribute.text)

with open("../data/mismatchRecords.csv", "w") as f:

    csvWriter = writer(f)

    for key, v in mismatchRecords.items():

        csvWriter.writerow(v)



