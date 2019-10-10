import os
import shutil
import errno
import sys
from datetime import datetime
from PIL import Image
import re



def isImage(file):
    if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".gif") or file.endswith(".raw") or file.endswith(".JPG") or file.endswith(".PNG") or file.endswith(".JPEG") or file.endswith(".GIF") or file.endswith(".RAW"):
        return True
    else:
        return False

def isVideo(file):
    if file.endswith(".avi") or file.endswith(".flv") or file.endswith(".wmv") or file.endswith(".mov") or file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".AVI") or file.endswith(".FLV") or file.endswith(".WMV") or file.endswith(".MOV") or file.endswith(".MP4") or file.endswith(".MKV"):
        return True
    else:
        return False


#Visit for details on Tag "https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif.html"
def get_date_taken(path):
    #print(path)

    try:
        extractedDate = Image.open(path)._getexif()[36867]
        if not extractedDate is None:
        #print("String: "+extractedDate)
            match = re.search(r'\d{4}:\d{2}:\d{2}', extractedDate)
            dateOut = datetime.strptime(match.group(), '%Y:%m:%d').date()
    except Exception:
        #print("No metadata Found, Copying to modified date path")
        return None

    return dateOut

# Variable Declarations
keepBothFiles = True
processVideoFiles = False



# Script start

if len(sys.argv) < 3:
    print('Usage "python3 copyFiles.py <source-path> <target-path>" options')
    print('WARNING: Do not put backslash at the end of the path')
    print('Options are: \n--keep-conflicts: keep files having same name\n--skip-conflicts: Skip file having same name\n--video: consider video files too')
    sys.exit(-1)
else: 
    sourceDir = sys.argv[1]
    targetDir = sys.argv[2]

if len(sys.argv) > 3:
    if sys.argv[3] == '--keep-conflicts':
        keepBothFiles = True
    elif sys.argv[3] == '--skip-conflicts':
        keepBothFiles = False
    elif sys.argv[3] == '--video':
        processVideoFiles = True
    else:
        print('Usage "python3 copyFiles.py <source-path> <target-path>" options')
        print('WARNING: Do not put backslash at the end of the path')
        print('Options are: \n--keep-conflicts: keep files having same name\n--skip-conflicts: Skip file having same name\n--video: consider video files too')
        sys.exit(-1)
        


if sourceDir.endswith("/"):
    sourceDir = sourceDir[:-1]
if not targetDir.endswith("/"):
    targetDir = targetDir + '/'

for root, dirs, files in os.walk(sourceDir):
    for file in files:
        if isImage(file) or isVideo(file):
            source = os.path.abspath(os.path.join(root, file))
            dest = targetDir + root.replace(sourceDir + '/', '') + '/'
            
            if isVideo(file):
                if not processVideoFiles:
                    continue
                else:
                    print("Video File")


            takenDate = get_date_taken(source)
            #print(takenDate)
            if not takenDate is None:
                dest = targetDir + str(takenDate.year) + "-" + str(takenDate.strftime("%m")) +"(" + takenDate.strftime("%b") + ")/"
            else:
                modified_time = datetime.fromtimestamp(os.stat(source).st_mtime)
                dest = targetDir + str(modified_time.year) + "-" + str(modified_time.strftime("%m")) +"(" + modified_time.strftime("%b") + ")/"

            if not processVideoFiles:
                if isVideo(file):
                    continue
            else:
                if isVideo(file):
                    dest += "Videos/"
                else:
                    dest += "Images/"
            
            #print("Destination path: " + dest) 
            if not os.path.exists(os.path.dirname(dest)):
                try:
                    #print("Destination created")
                    os.makedirs(os.path.dirname(dest))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            #print("Destination: " + dest + file)
            #print("Source: " + source)
            
            if not os.path.exists(dest + file):
                shutil.copy2(source,dest)
                print("File: " + source)
                print("Destination: " + dest + "\n")
            else:
                # Separate base from extension
                if keepBothFiles:
                    base, extension = os.path.splitext(file)
                    i = 1
                    while True:
                        new_name = os.path.join(dest, base + "_" + str(i) + extension)
                        if not os.path.exists(new_name):
                            shutil.copy2(source, new_name)
                            print ("Copied: " + base + extension +  " as: " + base + "_" + str(i) + extension)
                            break
                        i += 1
                else:
                    print('WARNING...!!!:\n' + source + ': Already exists\n')




