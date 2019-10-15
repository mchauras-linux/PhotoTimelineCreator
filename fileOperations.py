import os
import shutil
import datetime
import errno

#User Defined
import fileType

def performFileCopy(source, dest):
    size = os.path.getsize(source)
    print('Copying ' + str(size) + ' Bytes of Data')
    shutil.copy2(source,dest)
    print("File: " + source)
    print("Destination: " + dest + "\n")
    return size

def copyFile(source, destDir, file, skipConflicts):
    size = 0
    if not os.path.exists(destDir + file):
        size = performFileCopy(source, destDir)
    else:
        # Separate base from extension
        if not skipConflicts:
            base = fileType.getFileName(file)
            extension = fileType.getFileExtension(file)
            i = 1
            while True:
                new_name = os.path.join(destDir, base + "_" + str(i) + extension)
                if not os.path.exists(new_name):
                    size = performFileCopy(source, new_name)
                    break
                i += 1
        else:
            print('WARNING...!!!:\n' + source + ': Already exists\n')
    return size


def getDestFile(sourceFilePath, targetDir, takenDate, isFolderDepthDay):
    if takenDate is None:
        takenDate = datetime.datetime.fromtimestamp(os.stat(sourceFilePath).st_mtime)
    
    date = str(takenDate.year) + "-" + str(takenDate.strftime("%m"))
    dest = targetDir + date
    
    #Append Month as MMM
    dest += "(" + takenDate.strftime("%b") + ")"
    dest += "/"

    if isFolderDepthDay:
        dest += datetime.datetime.strftime(takenDate, '%d-%b-%Y') + "/"

    if fileType.isVideoFile(sourceFilePath):
        dest += "Videos/"    

    return dest


def createPath(dirToBeCreated):
    if not os.path.exists(os.path.dirname(dirToBeCreated)):
        try:
            os.makedirs(os.path.dirname(dirToBeCreated))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise