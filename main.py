import os
import shutil
from pprint import pprint


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
        return machineName + '_' + fileNameList[2][-2:] + fileNameList[2][:4] + fileNameList[-1]
    elif '.txt' in item:
        absolutePathList = item.split('\\')
        return absolutePathList[-1].replace('T', '').replace('.txt', '')


def moveFileAndRename(currentFile, previousFile):
    if currentFile[-3:] == 'jpg' and previousFile[-3:] == 'txt':
        with open(previousFile, 'r') as fp:
            line = fp.readlines()[0]

        line = line.replace('\n', '')
        currentFileList = currentFile.split('\\')
        n = len(currentFileList)
        currentFileName = currentFileList[n - 1]
        newFileName = currentFileName.replace(currentFileName[4:11], line)
        newFolderName = currentFileList[n - 2].replace('_convert', '')

        # 檢查是否有新資料夾之路徑(無包含convert之資料夾)，若沒有就創建
        if not os.path.isdir('\\'.join(currentFileList[:n - 2] + [newFolderName]) + '\\'):
            os.mkdir('\\'.join(currentFileList[:n - 2] + [newFolderName]) + '\\')

        # 從convert資料夾複製檔案到非convert資料夾
        shutil.copyfile(currentFile, '\\'.join(currentFileList[:n - 2] + [newFolderName] + [currentFileName]))

        # 重新命名圖片檔
        os.rename('\\'.join(currentFileList[:n - 2] + [newFolderName] + [currentFileName]),
                  '\\'.join(currentFileList[:n - 2] + [newFolderName] + [newFileName]))


if __name__ == '__main__':
    fileList = traversalSearch()
    fileListSorted = sorted(fileList, key=sortFunc)
    pprint(fileListSorted)
    for i in range(1, len(fileListSorted)):
        moveFileAndRename(fileListSorted[i], fileListSorted[i - 1])
