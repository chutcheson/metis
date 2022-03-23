from xml.etree.ElementTree import parse
from csv import reader, writer

# takes a path to XML document and uses it to make a table

def xmlToRecords(manifest):

    # create list to store records of vase images
    vaseRecords = []

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

        # check to see that there are images for vase
        if vaseID not in vases:

            # continue if no images
            continue

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

        # if all fields were present 
        if technique and provenance:

            # iterate over vase images
            for image in vases[vaseID]:

                # get image as numpy array
                imageArray = asarray(Image.open(image))

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

                else:

                    # if no channels
                    channels = 0
                    
                    # if no channels then image is grayscale
                    color = "GRAYSCALE"

                # add a row to vaseFileTable with vase info
                vaseFileTable.append([vaseID, image, technique, provenance.split(",")[0].split(" ")[0], height, width, channels, color])


# takes a path to a table
# returns a list of lists where each list stores image metadata

def getRecords(tablePath):

    # create list to store rows
    rows = []

    # open csv file
    with open(tablepath, "r") as f:

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
