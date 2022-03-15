from xml.etree.ElementTree import parse
from os import mkdir
from config import MANIFEST

# http://www.beazley.ox.ac.uk/Vases/SPIFF/Images200/GER37/CVA.GER37.1830.2/cc001001.jpe

tree = parse(MANIFEST)

= []

for vase in tree.getroot()[:2]:
    
    for attribute in vase:
        if attribute.tag == "URI":
            print(attribute.tag, attribute.text)
        if attribute.tag == "Image-Record":
            for img in attribute:
                if img.tag == "Filename":
                    imageURLS.append((img.tag, img.text))

print(imageURLS[:10])
