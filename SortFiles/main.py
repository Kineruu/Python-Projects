import time
import os

BasePath = os.path.dirname(os.path.abspath(__file__))
FilesFolder = os.path.join(BasePath, "images")

class SortFiles:
    def __init__(self, folder):
        self.folder = folder

    def renameByDate(self):
        try:
            files = os.listdir(self.folder)
            for item in files:
                itemPath = os.path.join(self.folder, item)

                if os.path.isfile(itemPath):
                    createdTime = os.path.getctime(itemPath)
                    readableTime = time.strftime("%d-%m-%Y %H-%M-%S", time.localtime(createdTime))

                    fileExtension = os.path.splitext(item)[1]
                    newItemName = f"{readableTime}{fileExtension}"
                    newPath = os.path.join(self.folder, newItemName)

                    number = 1
                    while os.path.exists(newPath):
                        newItemName = f"{readableTime}-{number}{fileExtension}"
                        newPath = os.path.join(self.folder, newItemName)
                        number += 1

                    os.rename(itemPath, newPath)
                    print(f"Renamed: {item} -> {newItemName}")
                    
        except FileNotFoundError:
            print(f"The file {item} does not exists!")
        except Exception as e:
            print(f"Error: {e}")

    def renameByExtension(self):
        try:
            files = os.listdir(self.folder)
            for item in files:
                itemPath = os.path.join(self.folder, item)

                if os.path.isfile(itemPath):
                    fileExtension = os.path.splitext(item)[1]
                    newItemName = f"{item}{fileExtension}"

                    newPath = os.path.join(self.folder, newItemName)

                    number = 1
                    while os.path.exists(newPath):
                        newItemName = f"{item}-{number}{fileExtension}"
                        newPath = os.path.join(self.folder, newItemName)
                        number += 1

                    os.rename(itemPath, newPath)
                    print(f"Renamed: {item} -> {newItemName}")

        except FileNotFoundError:
            print(f"The file {item} does not exists!")
        except Exception as e:
            print(f"Error: {e}")

    def renameBySize(self):
        try:
            files = os.listdir(self.folder)
            for item in files:
                itemPath = os.path.join(self.folder, item)

                if os.path.isfile(itemPath):
                    fileSize = os.path.getsize(itemPath)
                    readableSize = f"{fileSize} bytes"

                    fileExtension = os.path.splitext(item)[1]
                    newItemName = f"{readableSize}{fileExtension}"
                    newPath = os.path.join(self.folder, newItemName)

                    number = 1
                    while os.path.exists(newPath):
                        newItemName = f"{readableSize}-{number}{fileExtension}"
                        newPath = os.path.join(self.folder, newItemName)
                        number += 1

                    os.rename(itemPath, newPath)
                    print(f"Renamed: {item} -> {newItemName}")

        except FileNotFoundError:
            print(f"The file {item} does not exists!")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    sortFiles = SortFiles(FilesFolder)

    userOption = str(input("Enter the option (date, extension, size): "))
    userOption = userOption.lower()

    if userOption == "date":
        sortFiles.renameByDate()
    elif userOption == "extension":
        sortFiles.renameByExtension()
    elif userOption == "size":
        sortFiles.renameBySize()
    else:
        print("Invalid option! Try again.")
        quit()
