#Python Libs
import os

#User Libs
import argParser
import fileType
import timeUtil
import fileOperations
import sizeUtil
import duplicateUtils

def main():
    #Argument Parsing and Flags initialization
    args = argParser.parseCliArguments()
    print(args)
    sourceDir = args['source']
    targetDir = args['destination']
    fileTypeToBeProcessed = args['file_type']
    isFolderDepthDay = False
    skipConflicts = args['skip_conflicts']
    if args['folderLevel'] == 'd':
        isFolderDepthDay = True
    bigFileThreshold = sizeUtil.getSizeInBytes(args['big_file_size'])
    keepDuplicates = args['keep_duplicates']

    #Iterating Recursively through the source path
    for root, dirs, files in os.walk(sourceDir):
        for file in files:
            #generate Source File Path from root
            sourceFilePath = os.path.abspath(os.path.join(root, file))
            if fileType.isValidFileToProcess(sourceFilePath, fileTypeToBeProcessed):
                #Generate Dest File Path form root
                destinationDir = fileOperations.getDestFile(sourceFilePath, targetDir, timeUtil.get_date_taken(sourceFilePath), isFolderDepthDay)
                fileOperations.createPath(destinationDir)
                fileOperations.copyFile(sourceFilePath, destinationDir, file, skipConflicts)

    if not keepDuplicates:
        print()
        print("*************************************************************")
        print("                Removing Duplicates")
        print("*************************************************************")
        duplicateUtils.removeDuplicates([targetDir])
        print()
        print("*************************************************************")
        print("                 Duplicates Removed")
        print("*************************************************************")

    print("*************************************************************")
    print("                Files Greater Than "+ sizeUtil.getHumanReadableSize(bigFileThreshold))
    count = sizeUtil.getFilesLargerThan(targetDir, bigFileThreshold)
    if(count == 0):
        print("              No file is larger than "+ sizeUtil.getHumanReadableSize(bigFileThreshold))
    print("*************************************************************")

if __name__ == "__main__":
    main()