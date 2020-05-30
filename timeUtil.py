from PIL import Image
import re
from datetime import datetime
import os

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

def get_time_taken(path):
    try:
        extractedTime = Image.open(path)._getexif()[36867].split()[1]
        timeOut = datetime.strptime(extractedTime, '%H:%M:%S').time()
        print(timeOut)
    except Exception:
        #print("No metadata Found, Copying to modified date path")
        stat = os.stat(path)
        #timeOut = datetime.strptime(stat.st_mtime, '%H:%M:%S').time()
        timeOut = datetime.fromtimestamp(stat.st_mtime).strftime('%H:%M:%S')
        timeOut = datetime.strptime(timeOut, '%H:%M:%S')
    return timeOut