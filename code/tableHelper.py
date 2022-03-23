from csv import reader, writer

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
