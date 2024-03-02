from zipfile import ZipFile
from pathlib import Path

"""step one - creation of a folder and files"""
""" Path('my-files').mkdir()

with open("my-files/first.txt", "w") as my_file:
    my_file.write("First file")

with open("my-files/second.txt", "w") as my_file:
    my_file.write("Second file") """

""""step two - zip"""
with ZipFile("my-files.zip", mode="w") as my_zip_file:
    for file in Path("my-files").iterdir():
        """ print(file) """
        my_zip_file.write(file)

"""step three - unzip"""
print(my_zip_file.infolist())

with ZipFile("my-files.zip") as my_zip_file:
    my_zip_file.extractall("my-files-second")
