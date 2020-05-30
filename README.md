# PhotoTimelineCreator
Create a timeline based on when the photo is clicked

# View This README as RAW

usage: main.py [-h] -s SOURCE -d DESTINATION [-c] [-v] [-l {d,m}] [-k] [-f [{image,video} [{image,video} ...]]] [-b BIG_FILE_SIZE]

Copy Video and Images in a timeline like folder structure

optional arguments:
  -h, --help            show this help message and exit
  -s SOURCE, --source SOURCE
                        Path to source Directory
  -d DESTINATION, --destination DESTINATION
                        Path to destination Directory
  -c, --skip-conflicts  Skip file having same name.
  -v, --video           Copy video files too
  -l {d,m}, --level {d,m}
                        Level of file Directories to be created. {d - Days Level, m - Month Level}
  -k, --keep-duplicates
                        Keep the files with same content irrespective of file Name
  -f [{image,video} [{image,video} ...]], --file-type [{image,video} [{image,video} ...]]
                        File types to be copied
  -b BIG_FILE_SIZE, --big-file-size BIG_FILE_SIZE
                        Print Files which are greater than the mentioned size

Thank You...!!!
