import zipfile
import shutil
import os
from zhtools import simple2tradition


def zip_archive(sFilePath, dst=""):
    """
    input : Folder path and name
    output: using zipfile to ZIP folder
    """
    if dst == "":
        zf = zipfile.ZipFile(sFilePath + '.ZIP', mode='w')
    else:
        zf = zipfile.ZipFile(dst, mode='w')

    os.chdir(sFilePath)
    # print sFilePath
    for root, folders, files in os.walk(".\\"):
        for sfile in files:
            aFile = os.path.join(root, sfile)
            # print aFile
            zf.write(aFile)
    zf.close()


def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def find_file_list(folder: str) -> None:
    extension = ('.html', '.css', '.dat', 'xml', '.txt', '.ncx', '.opf', '.xhtml')
    file_list = [folder + '\\' + each for each in os.listdir(folder) if each.endswith(extension)]
    all_file_list.extend(file_list)
    folder_list = [os.path.join(folder, o) for o in os.listdir(folder) if
                   os.path.isdir(os.path.join(folder, o))]
    if len(folder_list) > 0:
        print('folder_list', folder_list)
        for sub_dir in folder_list:
            find_file_list(sub_dir)
    else:
        return


FILE_PATH = r'C:/Users/Curry/Desktop/Unknown/Cheng Xu Yuan De Zi Wo Xiu Yang/Cheng Xu Yuan De Zi Wo Xiu Yang  - Leo Hui.epub'

file_name = FILE_PATH.split('/')[-1].split('.')[0]
print(file_name)
all_file_list = []
create_dir('temp_old')
create_dir('temp_new')
extract_path = 'temp_old\\' + file_name
compress_path = 'temp_new\\' + file_name
create_dir(extract_path)
create_dir(compress_path)

# 解壓縮epub檔案
with zipfile.ZipFile(FILE_PATH) as zp:
    zp.extractall(extract_path)

# 建立檔案清單
find_file_list(extract_path)

# 複製整個資料夾
copytree(extract_path, compress_path)

for file_path_old in all_file_list:
    with open(file_path_old, 'r', encoding='utf-8') as f:
        test_cn = f.read()
    test_tw = simple2tradition(test_cn)
    file_path_new = file_path_old.replace(extract_path, compress_path)
    # print('new_filePath')
    with open(file_path_new, 'w', encoding='utf-8') as f:
        # print('save', file_path_new)
        f.write(test_tw)

# 壓縮檔案，建立epub
zip_archive(compress_path, file_name + '.epub')
