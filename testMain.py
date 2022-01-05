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


def getTextFilesPath():
    return traversalSearch(os.getcwd(), '.txt')


def getImageFilesPath():
    return traversalSearch(os.getcwd(), '.jpg')


def sortFunc(item):

    pass


def recordFilesName2DataFrame(imageFilesPathList, textFilesPathList):
    def generateFilesNameList(filesPathList, func):
        filesNameList = list()
        for filePath in filesPathList:
            filesNameList.append(func(filePath))
        return filesNameList

    recordList = list()

    imageFilesNameList = generateFilesNameList(imageFilesPathList, getFileNameFromAbsolutePath)
    textFilesNameList = generateFilesNameList(textFilesPathList, getFileNameFromAbsolutePath)

    imageWithTextFilesPathList = imageFilesPathList + textFilesPathList
    imageWithTextFilesNameList = imageFilesNameList + textFilesNameList

    for filePath, fileName in zip(imageWithTextFilesPathList, imageWithTextFilesNameList):
        recordList.append(
            [filePath, fileName]
        )

    return recordList


def getFileNameFromAbsolutePath(absoluteFilePath):
    absoluteFilePathList = absoluteFilePath.split('/')
    n = len(absoluteFilePathList)
    return absoluteFilePathList[n - 1]


def moveFile():
    pass


if __name__ == '__main__':
    textFilesPathList = getTextFilesPath()
    imageFilesPathList = getImageFilesPath()
    recordList = recordFilesName2DataFrame(imageFilesPathList, textFilesPathList)
    pprint(recordList)
    recordList = sortFunc(recordList)
