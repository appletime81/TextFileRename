import os
import pandas as pd

from pprint import pprint


def traversalSearch(currentPath, extension):
    filesList = list()
    for home, dirName, files in os.walk(currentPath):
        for file in files:
            if os.path.isfile(os.path.join(home, file)) and file[-4:] == extension:
                filesList += [os.path.join(home, file).replace('\\', '/')]
    return filesList


def getTextFiles():
    return traversalSearch(os.getcwd(), '.txt')


def getImageFiles():
    return traversalSearch(os.getcwd(), '.jpg')


def recordFilesName2DataFrame(imageFilesList, textFilesList):
    pass


def getFileNameFromAbsolutePath(absoluteFilePath):
    absoluteFilePathList = absoluteFilePath.split('/')
    n = len(absoluteFilePathList)
    return absoluteFilePathList[n - 1]


def moveFile():
    pass


if __name__ == '__main__':
    # pprint(getTextFiles())
    textFilesList = getTextFiles()
    # with open(textFilesList[len(textFilesList) - 1], 'r') as fp:
    #     lines = fp.readlines()

    print('-------------------------------------------------------------------')
    # pprint(lines)

    fileName = getFileNameFromAbsolutePath(textFilesList[len(textFilesList) - 1])
    print(fileName)