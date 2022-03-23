from random import sample
from math import floor

def getVaseTypes(vaseMetadataDict, vaseImages):

    redFigure = []
    blackFigure = []

    for vase in vaseImages:

        vaseStyle = vaseMetadataDict[vase][1]

        if vaseStyle == "RED-FIGURE":

            redFigure.append(vase)

        elif vaseStyle == "BLACK-FIGURE":

            blackFigure.append(vase)

        else:

            pass

    return (redFigure, blackFigure)

def performSplit(redFigureVases, blackFigureVases, validation_size = .2):

    training = set()
    training.update(sample(redFigureVases, floor(len(redFigureVases) * (1 - validation_size))))
    training.update(sample(blackFigureVases, floor(len(blackFigureVases) * (1 - validation_size))))

    validation = set()
    validation.update(set(redFigureVases) - training)
    validation.update(set(blackFigureVases) - training)

    return (training, validation)
