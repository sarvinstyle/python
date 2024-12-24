from zipfile import ZipFile
from pathlib import Path

with ZipFile("lesson13\\zip1.zip" , "w") as zip:
    for path in Path("lesson13\\docs").rglob("*.*"):
        zip.write(path)


with ZipFile("lesson13\\zip1.zip" , "r") as zip :
    print(zip.namelist())
    zip.extractall("lesson13\\extract")