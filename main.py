import os
import shutil
from pprint import pprint


def sort_func(file_name):
    if ".jpg" in file_name:
        return file_name[-13:-11] + file_name[-19:-15] + file_name[-10:-4]
    elif ".txt" in file_name:
        return file_name[-16:-4]


def get_all_files():
    files_list = []
    for home, dirName, files in os.walk(os.getcwd()):
        for file in files:
            files_list += [os.path.join(home, file)]
    files_list = [file for file in files_list if ("txt" in file or "jpg" in file)]
    files_list = sorted(files_list, key=sort_func)
    return files_list


def rename_files(files):
    sub_file_name = ""
    image_file_list = []
    log_file = "log.txt"
    image_files = load_log_file(log_file)

    for i, file in enumerate(files):
        if file in image_files:
            pass
        else:
            if i == 0 and "jpg" in file:
                os.rename(file, file.replace(file[-27:-20], "ERROR"))

                # 紀錄已被處理過的檔案
                image_file_list.append(file.replace(file[-27:-20], "ERROR") + "\n")
            elif "txt" in file:
                with open(file, "r") as f:
                    line = f.readline()
                    x2 = line[0:7]
                sub_file_name = x2
                #sub_file_name = line
            elif "jpg" in file:
                file_name = file.replace(file[-27:-20], sub_file_name)
                target_path = file_name.replace("_convert", "")
                pprint([file_name, target_path])

                # 移動檔案
                try:
                    shutil.copy(file, target_path)
                except shutil.SameFileError:
                    continue

                # 紀錄已被處理過的檔案
                image_file_list.append(file + "\n")

    # 被處理過的檔案儲存至log.txt紀錄
    save_log_file(image_file_list)


def save_log_file(record_list):
    with open("log.txt", "a") as f:
        f.writelines(record_list)


def load_log_file(log_file):
    # 打開log.txt比對是否有已被記錄過的檔案
    try:
        with open(log_file, "r") as f:
            image_files = f.readlines()
    except FileNotFoundError:
        # 如果沒有log.txt檔
        # 建立log.txt
        with open(log_file, "w") as f:
            pass
        with open(log_file, "r") as f:
            image_files = f.readlines()

    image_files = [image_file.strip() for image_file in image_files]
    return image_files


if __name__ == "__main__":
    all_files = get_all_files()
    rename_files(all_files)
