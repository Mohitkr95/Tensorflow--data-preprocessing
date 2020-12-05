import xml.etree.ElementTree as obj
from glob import glob
import os

def updateXML(filename):
    tree = obj.ElementTree(file = filename)
    root = tree.getroot()

    for name in root.iter("name"):
        if name.text == "tyre": 
            name.text = "white"
        if name.text == "helmet":
            name.text = "yellow"
        
            
    tree = obj.ElementTree(root)

    with open(filename, "wb") as fileupdate:
        tree.write(fileupdate)


if __name__ == "__main__":
    directory = r'D:\Final PPE Data\Yellow'
    i=1
    for files in os.listdir(directory):
        if files.endswith(".xml"):
            updateXML(files)
