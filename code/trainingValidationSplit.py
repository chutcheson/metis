from config import IMAGE_TABLE
from collections import Counter
from random import sample
from math import floor
from csv import reader, writer

with open(IMAGE_TABLE, "r") as f:
    
    imageTable = []
    
    for shard in reader(f):

        if shard[2] == "RED-FIGURE" or shard[2] == "BLACK-FIGURE":

            imageTable.append(shard)

vases = { shard[0] : shard[2] for shard in imageTable }
vaseCounter = Counter([shard[0] for shard in imageTable])

validation_vases = set(sample(list(vases), k = floor(len(vases) * .2)))
training_vases = set(vases.keys()) - validation_vases

redFigure = 0
blackFigure = 0

for vase in validation_vases:

    if vases[vase] == 'RED-FIGURE':

        redFigure += vaseCounter[vase]

    else:

        blackFigure += vaseCounter[vase]

print(f"validation - black-figure:{blackFigure}, red-figure:{redFigure}, ratio:{blackFigure/redFigure}")

trainingRedFigure = 0
trainingBlackFigure = 0

for vase in training_vases:

    if vases[vase] == 'RED-FIGURE':

        trainingRedFigure += vaseCounter[vase]

    else:

        trainingBlackFigure += vaseCounter[vase]

print(f"training - black-figure:{trainingBlackFigure}, red-figure:{trainingRedFigure}, ratio:{trainingBlackFigure/trainingRedFigure}")

for row in imageTable:

    if row[0] in validation_vases:

        row.append("validation")

    else:

        row.append("training")

with open(IMAGE_TABLE + "Split", "w") as f:

    csvWriter = writer(f)

    for row in imageTable:
        
        csvWriter.writerow(row)
