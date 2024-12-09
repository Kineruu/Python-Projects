import time
import os

BasePath = os.path.dirname(os.path.abspath(__file__))
FilesFolder = os.path.join(BasePath, "images")

def renameByDate(folder):
    try:
        files = os.listdir(folder)
        for item in files:
            itemPath = os.path.join(folder, item)

            if os.path.isfile(itemPath):
                createdTime = os.path.getctime(itemPath)
                readableTime = time.strftime("%d-%m-%Y %H-%M-%S", time.localtime(createdTime))

                fileExtension = os.path.splitext(item)[1]
                newItemName = f"{readableTime}{fileExtension}"
                newPath = os.path.join(folder, newItemName)

                number = 1
                while os.path.exists(newPath):
                    newItemName = f"{readableTime}-{number}{fileExtension}"
                    newPath = os.path.join(folder, newItemName)
                    number += 1

                os.rename(itemPath, newPath)
                print(f"Renamed: {item} -> {newItemName}")
                
    except FileNotFoundError:
        print(f"The file {item} does not exists!")
    except Exception as e:
        print(f"Error: {e}")

renameByDate(FilesFolder)
