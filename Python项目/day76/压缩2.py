import os
import zipfile
def zip_file(filepath,targtepath=None):
    """

    :param filepath: 待压缩文件/文件夹
    :param targtepath: 压缩文件存储位置
    :return:
    """
    base_dir ,file_name = os.path.split(filepath)
    zip_name = file_name.split('.')[0]+'.zip'
    f = zipfile.ZipFile(os.path.join(targtepath or base_dir, zip_name), 'w', zipfile.ZIP_DEFLATED)
    if os.path.isfile(filepath):
        f.write(filepath,file_name)
        return
    else:
        for dir_path, dir_name, file_names in os.walk(filepath):
            # 要是不replace，就从根目录开始复制
            file_path = dir_path.replace(base_dir, '')
            # 实现当前文件夹以及包含的所有文件
            file_path = file_path and file_path + os.sep or ''
            for file_name in file_names:
                f.write(os.path.join(dir_path, file_name), file_path + file_name)
    f.close()
zip_file(r'C:\Users\24479\Desktop\作业上传\Python项目\day76\dirfiles',r'C:\Users\24479\Desktop\TEST')