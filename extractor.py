# Author @salmanually:github: hotheadhacker
from zipfile import ZipFile

# File Name
file_name = "sample.zip"

# opening the zip file
with ZipFile(file_name, "r") as zip:
    # Print all files inside zip
    zip.printdir()

    # Extracting files inside zip
    print("Extracting files from the zip... \n")
    zip.extractall()
    print("Success! Files have been extracted")
