import os
import sys

KB_VALUE = 1024
MB_VALUE = KB_VALUE * 1024
GB_VALUE = MB_VALUE * 1024

compareSize = False

def getHumanReadableSize(size):
    humanSize = size
    if size >= GB_VALUE:
        humanSize = size/GB_VALUE
        return str(round(humanSize, 1)) + 'GB'
    elif size >= MB_VALUE:
        humanSize = size/MB_VALUE
        return str(round(humanSize, 1)) + 'MB'
    elif size >= KB_VALUE:
        humanSize = size/KB_VALUE
        return str(round(humanSize, 1)) + 'KB'
    else:
        return str(size) + 'B'

def getSizeInBytes(size):
    if size.endswith('GB'):
        return int(size[:-2]) * GB_VALUE
    if size.endswith('MB'):
        return int(size[:-2]) * MB_VALUE
    if size.endswith('KB'):
        return int(size[:-2]) * KB_VALUE
    if size.endswith('B'):
        return int(size[:-1])
    return int(size)

def getFilesLargerThan(path, size):
    sizeInBytes = getSizeInBytes(str(size))
    #print(sizeInBytes)
    for root, dirs, files in os.walk(path):
        for file in files:
            filePath = os.path.abspath(os.path.join(root, file))
            fileSizeInBytes = os.path.getsize(filePath)
            if fileSizeInBytes > sizeInBytes:
                fileSizeReadable = getHumanReadableSize(fileSizeInBytes)
                print('\nFile Size: ' + fileSizeReadable + '\n' + filePath)

def main():
    if len(sys.argv) == 2:
        getFilesLargerThan(sys.argv[1], '0')
    elif len(sys.argv) == 3:
        getFilesLargerThan(sys.argv[1], sys.argv[2])
    else:
        print('Usage python3 sizeUtil.py <Directory> <Size>')

if __name__ == "__main__":
    main()