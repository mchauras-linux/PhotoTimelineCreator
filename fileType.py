import os

#Constants
IMAGE_FILE = 'image'
VIDEO_FILE = 'video'

#Supported File types
#Just add extension to support file type
imageFileList = [".jpg", ".png", ".jpeg", ".gif", ".raw"]
videoFileList = [".avi", ".flv", ".wmv", ".mov", ".mp4", ".mkv"]


def isVideoFile(fileToBeProcessed):
    if getFileExtension(fileToBeProcessed) in videoFileList:
        return True
    else:
        return False


def isImageFile(fileToBeProcessed):
    if getFileExtension(fileToBeProcessed) in imageFileList:
        return True
    else:
        return False


def getFileExtension(fileToBeProcessed):
    filename, file_extension = os.path.splitext(fileToBeProcessed)
    return file_extension.lower()


def getFileName(fileToBeProcessed):
    filename, file_extension = os.path.splitext(fileToBeProcessed)
    return filename


def isValidFileToProcess(fileToBeProcessed, listOfValidFileTypes):
    #For Image File
    if IMAGE_FILE in listOfValidFileTypes:
        if getFileExtension(fileToBeProcessed) in imageFileList:
            return True
    
    if VIDEO_FILE in listOfValidFileTypes:
        if getFileExtension(fileToBeProcessed) in videoFileList:
            return True

    return False
