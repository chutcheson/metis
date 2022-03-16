from pathlib import Path
from config import IMAGES
from hashlib import md5

def md5file(fileName):

    with open(fileName, "rb") as f:
        file_hash = md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)

    return file_hash.hexdigest()

pathlist = Path(IMAGES).glob('**/*')
folders = []

for index, path in enumerate(pathlist):
    
    folders.append(path)

images = []
prevHashes = {}

for index, folder in enumerate(folders):

    folderImages = folder.glob('**/*')

    folderImages = [image for image in folder.glob('**/*')]

    hashes = [md5file(str(image)) for image in folderImages]

    seen = {}

    for image, h in zip(folderImages, hashes):

        if h in seen:

            print(f"collision: {str(image)} and {seen[h]}")

        elif h in prevHashes:

            print(f"collision: {str(image)} and {prevHashes[h]}")
        
        else:

            seen[h] = str(image)

    prevHashes.update(seen)

