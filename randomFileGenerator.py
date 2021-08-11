#!/usr/bin/python

import sys
import getopt

outputFileName = "randomFile.txt"

def main(argv):
    print("Random File Generator")
    print("This script will generate files with random contents")
    args = sys.argv[1:]
    if args[0] == '-h':
        print('test.py <filesize>')
        sys.exit()
    elif len(sys.argv) > 1:
        fileSize = int(args[0])
        print('New file size is ', fileSize)
        generateRandomLetters(outputFileName, fileSize)

def generateRandomLetters(filename,size):
    """
    generate big random letters/alphabets to a file
    :param filename: the filename
    :param size: the size in bytes
    :return: void
    """
    import random
    import string

    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)]) #1

    with open(filename, 'w') as f:
        f.write(chars)
    pass
    print("Generated the file", filename)


if __name__ == "__main__":
    main(sys.argv[1:])