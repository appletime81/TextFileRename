import os
from pprint import pprint
from datetime import datetime

a = 'TOP_1939741_11072021_125548.jpg'


def convert2TimeStr(fileName):
    fileNameList = fileName.split('_')
    fileNameList[len(fileNameList) - 1] = fileNameList[len(fileNameList) - 1][:-4]
    # print(fileNameList[len(fileNameList) - 1])
    yearStr = fileNameList[2][-4:]
    dateStr = fileNameList[2][:4]
    hrMinSecStr = fileNameList[3]
    dateTimeStr = yearStr + dateStr + hrMinSecStr
    print(f'dateTimeStr: {dateTimeStr}')
    dateTime = datetime.strptime(dateTimeStr, '%Y%m%d%H%M%S')

    print(f'yearStr: {yearStr}')
    print(f'dateTime: {dateTime}')


def traversalSearch():
    fileList = list()
    for home, dirName, files in os.walk(os.getcwd()):
        for file in files:
            if os.path.isfile(os.path.join(home, file)) and file[-4:] in ['.txt', '.jpg']:
                fileList += [os.path.join(home, file)]
    return fileList


def sortFunc(item):
    if '.jpg' in item:
        absolutePathList = item.split('\\')
        machineNameList = absolutePathList[-2].split('_')
        machineName = machineNameList[0] + '-' + machineNameList[1]
        fileName = absolutePathList[-1].replace('.jpg', '')
        fileNameList = fileName.split('_')
        print(machineName + '_' + fileNameList[2][-4:] + fileNameList[2][:4] + fileNameList[-1])
        return machineName + '_' + fileNameList[2][-2:] + fileNameList[2][:4] + fileNameList[-1]
    elif '.txt' in item:
        absolutePathList = item.split('\\')
        print(absolutePathList[-1].replace('T', '').replace('.txt', ''))
        return absolutePathList[-1].replace('T', '').replace('.txt', '')


if __name__ == '__main__':
    fileList = traversalSearch()
    fileListSorted = sorted(fileList, key=sortFunc)
    pprint(fileListSorted)

