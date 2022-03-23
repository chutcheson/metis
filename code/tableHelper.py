from xml.etree.ElementTree import parse
from csv import reader, writer
from collections import defaultdict

# takes vase metadata and vase imagepaths
# makes records for a table using metadata and imagepaths

def makeTableRecords(vaseMetadataDict, vaseImages):

    # list to hold records
    table = []

    # iterate over vases with images
    for vase in vaseImages:

        # iterate over individual vases
        for image in vaseImages[vase]:

            # append images to metadata for vase
            table.append(vaseMetadataDict[vase] + [image])

    # return table records
    return table

# takes a path to XML document and uses it to make a table

def xmlToVaseDict(manifest):

    # create list to store records of vase images
    vaseDict = {}

    # create XML tree of vases
    tree = parse(manifest)

    # iterate over vases
    for vase in tree.getroot():

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

        # iterate over vase attributes
        for child in vase:

            # check for technique
            if child.tag == "Technique":

                technique = child.text

            # check for provenance
            elif child.tag == "Provenance":

                provenance = child.text

            else:

                pass

        # add a row to vaseFileTable with vase info
        vaseDict[vaseID] = [vaseID, technique]

        if provenance:

            vaseDict[vaseID].append(provenance.split(",")[0].split(" ")[0])

        else:

            vaseDict[vaseID].append(None)

    return vaseDict 

# takes a path to a table
# returns a list of lists where each list stores image metadata

def getRecords(tablePath):

    # create list to store rows
    rows = []

    # open csv file
    with open(tablePath, "r") as f:

        # iterate over the rows
        for image in reader(f):

            # append list row to list
            rows.append(image)

    # return rows
    return rows

# takes a list of records and a path to place table
# stores table at tablePath

def recordsToTable(records, tablePath):

    # open file to write to
    with open(tablePath, "w") as f:

        # create csv writer
        csvWriter = writer(f)

        # iterate over rows
        for row in records:

            # write rows to csv
            csvWriter.writerow(row)
