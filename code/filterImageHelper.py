# takes a list of rows 
# filters the images based upon image size

def filterSize(records, imageSize):

    # create a list to store remaining records
    filteredImages = []

    # iterate over the image table records
    for image in records:

        # check to see if image meets minimum size
        if int(image[4]) >= imageSize and int(image[5]) >= imageSize:

            # append image to list
            filteredImages.append(image)

    # return list of images
    return filteredImages

# takes a list of records 
# filters the images based upon color

def filterColor(records, color):

    # create a list to store remaining records
    filteredImages = []

    # iterate over the image table records
    for image in records:

        if image[7] == color: 
            
            # keep record
            filteredImages.append(image)

    # return a list of images
    return filteredImages
