import argparse

#User Defined
import fileType

def parseCliArguments():
    parser = argparse.ArgumentParser(description="Copy Video and Images in a timeline like folder structure", epilog="Thank You...!!!\n")
    parser.add_argument("-s", "--source", required=True, help="Path to source Directory")
    parser.add_argument("-d", "--destination", required=True, help="Path to destination Directory")
    parser.add_argument("-c", "--skip-conflicts", action='store_true', help='Skip file having same name.')
    parser.add_argument("-v", "--video", action='store_true', help='Copy video files too')
    parser.add_argument("-l", "--level", choices=['d', 'm'], default='m', dest='folderLevel', help="Level of file Directories to be created. {d - Days Level, m - Month Level}")
    parser.add_argument("-k", "--keep-duplicates", action='store_true', help='Keep the files with same content irrespective of file Name')
    parser.add_argument("-f", "--file-type", nargs='*', choices=[fileType.IMAGE_FILE, fileType.VIDEO_FILE], default=[fileType.IMAGE_FILE], help="File types to be copied")
    parser.add_argument("-b", "--big-file-size", default='1000GB', help="Print Files which are greater than the mentioned size")
    args = vars(parser.parse_args())
    formatDirectoryPath(args)
    parseFileTypeToBeProcessed(args)
    return args

def formatDirectoryPath(args):
    if not args['source'].endswith("/"):
        args['source'] = args['source'] + '/'
    if not args['destination'].endswith("/"):
        args['destination'] = args['destination'] + '/'

def parseFileTypeToBeProcessed(args):
    if args['video']:
        args['file_type'].append(fileType.VIDEO_FILE)