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


convert2TimeStr(a)
